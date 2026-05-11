import copy

from psycopg2.extras import Json

from .db import get_cursor
from .payload_generator_one_form import generate_payload
from .structure_service import (
    activate_version,
    compute_hash,
    get_active_structure,
    validate_draft,
)


def _split_path(json_path):
    parts = [p for p in json_path.split(".") if p]
    if not parts:
        raise ValueError("json_path cannot be empty")
    return parts


def _get_by_path(document, json_path):
    cur = document
    for part in _split_path(json_path):
        if not isinstance(cur, dict) or part not in cur:
            raise ValueError(f"Path not found: {json_path}")
        cur = cur[part]
    return cur


def _set_by_path(document, json_path, value):
    parts = _split_path(json_path)
    cur = document
    for part in parts[:-1]:
        if part not in cur or not isinstance(cur[part], dict):
            cur[part] = {}
        cur = cur[part]
    cur[parts[-1]] = value


class OneFormServiceAPI:
    def __init__(self, form_type="ITR6_BASIC", actor="api_user"):
        self.form_type = form_type
        self.actor = actor

    def create_draft_from_active(self, next_major=None, next_minor=None):
        active = get_active_structure(self.form_type)
        schema = copy.deepcopy(active["schema_json"])
        major = active["version_major"] if next_major is None else next_major
        minor = next_minor
        if minor is None:
            with get_cursor() as (_, cur):
                cur.execute(
                    """
                    SELECT COALESCE(MAX(version_minor), -1)
                    FROM payload_structure
                    WHERE form_type = %s AND version_major = %s
                    """,
                    (self.form_type, major),
                )
                minor = cur.fetchone()[0] + 1
        schema_hash = compute_hash(schema)

        with get_cursor() as (_, cur):
            cur.execute(
                """
                INSERT INTO payload_structure (
                    form_type, version_major, version_minor, status, is_active,
                    schema_json, schema_hash, validation_report, created_by, updated_by
                )
                VALUES (%s, %s, %s, 'draft', FALSE, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    self.form_type,
                    major,
                    minor,
                    Json(schema),
                    schema_hash,
                    Json({"valid": False, "errors": ["Draft not validated yet"]}),
                    self.actor,
                    self.actor,
                ),
            )
            draft_id = cur.fetchone()[0]
        return draft_id

    def update_node(self, draft_id, json_path, node_payload):
        with get_cursor() as (_, cur):
            cur.execute(
                """
                SELECT schema_json, form_type, version_major, version_minor
                FROM payload_structure
                WHERE id = %s AND status = 'draft'
                """,
                (draft_id,),
            )
            row = cur.fetchone()
            if not row:
                raise ValueError("Draft not found or not editable")

            schema_json, form_type, vmaj, vmin = row
            old_value = None
            try:
                old_value = _get_by_path(schema_json, json_path)
            except ValueError:
                old_value = None

            _set_by_path(schema_json, json_path, node_payload)
            new_hash = compute_hash(schema_json)

            cur.execute(
                """
                UPDATE payload_structure
                SET schema_json = %s,
                    schema_hash = %s,
                    updated_by = %s,
                    updated_at = NOW()
                WHERE id = %s
                """,
                (Json(schema_json), new_hash, self.actor, draft_id),
            )
            cur.execute(
                """
                INSERT INTO payload_structure_audit (
                    structure_id, form_type, version_major, version_minor, change_type,
                    json_path, old_value, new_value, changed_by, request_id
                )
                VALUES (%s, %s, %s, %s, 'node_update', %s, %s, %s, %s, %s)
                """,
                (
                    draft_id,
                    form_type,
                    vmaj,
                    vmin,
                    json_path,
                    Json(old_value) if old_value is not None else None,
                    Json(node_payload),
                    self.actor,
                    f"upd_{draft_id}_{json_path}",
                ),
            )

    def validate(self, draft_id):
        return validate_draft(draft_id, actor=self.actor)

    def activate(self, draft_id):
        activate_version(draft_id, actor=self.actor)

    def generate(self, source_payload):
        active = get_active_structure(self.form_type)
        return generate_payload(active["schema_json"], source_payload)
