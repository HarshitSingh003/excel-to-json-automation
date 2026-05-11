import hashlib
import json

from psycopg2.extras import Json

from .db import get_cursor
from .schema_validator import validate_structure


def compute_hash(schema_json):
    canonical = json.dumps(schema_json, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def create_draft(form_type, version_major, version_minor, schema_json, actor="system"):
    schema_hash = compute_hash(schema_json)
    validation = {"valid": False, "errors": ["Draft not validated yet"]}

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
                form_type,
                version_major,
                version_minor,
                Json(schema_json),
                schema_hash,
                Json(validation),
                actor,
                actor,
            ),
        )
        return cur.fetchone()[0]


def validate_draft(structure_id, actor="validator"):
    with get_cursor() as (_, cur):
        cur.execute(
            """
            SELECT schema_json
            FROM payload_structure
            WHERE id = %s
            """,
            (structure_id,),
        )
        row = cur.fetchone()
        if not row:
            raise ValueError("structure_id not found")

        report = validate_structure(row[0])
        new_status = "validated" if report["valid"] else "draft"

        cur.execute(
            """
            UPDATE payload_structure
            SET status = %s,
                validation_report = %s,
                updated_by = %s,
                updated_at = NOW()
            WHERE id = %s
            """,
            (new_status, Json(report), actor, structure_id),
        )
        return report


def activate_version(structure_id, actor="admin"):
    with get_cursor() as (_, cur):
        cur.execute(
            """
            SELECT form_type, status, version_major, version_minor
            FROM payload_structure
            WHERE id = %s
            """,
            (structure_id,),
        )
        row = cur.fetchone()
        if not row:
            raise ValueError("structure_id not found")

        form_type, status, version_major, version_minor = row
        if status not in ("validated", "active"):
            raise ValueError("Only validated structure can be activated")

        cur.execute(
            "UPDATE payload_structure SET is_active = FALSE WHERE form_type = %s",
            (form_type,),
        )
        cur.execute(
            """
            UPDATE payload_structure
            SET is_active = TRUE, status = 'active', updated_by = %s, updated_at = NOW()
            WHERE id = %s
            """,
            (actor, structure_id),
        )
        cur.execute(
            """
            INSERT INTO payload_structure_audit (
                structure_id, form_type, version_major, version_minor,
                change_type, json_path, old_value, new_value, changed_by, request_id
            )
            VALUES (%s, %s, %s, %s, 'activate', '$', NULL, %s, %s, %s)
            """,
            (
                structure_id,
                form_type,
                version_major,
                version_minor,
                Json({"activated": True}),
                actor,
                f"activate_{structure_id}",
            ),
        )


def get_active_structure(form_type):
    with get_cursor() as (_, cur):
        cur.execute(
            """
            SELECT id, version_major, version_minor, schema_json
            FROM payload_structure
            WHERE form_type = %s AND is_active = TRUE
            ORDER BY version_major DESC, version_minor DESC
            LIMIT 1
            """,
            (form_type,),
        )
        row = cur.fetchone()
        if not row:
            raise ValueError(f"No active structure found for form_type={form_type}")
        return {
            "id": row[0],
            "version_major": row[1],
            "version_minor": row[2],
            "schema_json": row[3],
        }
