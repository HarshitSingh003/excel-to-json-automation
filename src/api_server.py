import json
import os
from datetime import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from psycopg2.extras import Json

from .db import get_cursor
from .excel_adapter import parse_excel_to_source_payload
from .legacy_node_migrator import load_full_legacy_bundle, load_legacy_root_node
from .legacy_exact_from_file import generate_legacy_exact_json
from .missing_nodes_bundle_tools import build_missing_nodes_bundle
from .parity_checker import compare_with_legacy
from .service_api import OneFormServiceAPI


class DraftRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    next_major: int | None = None
    next_minor: int | None = None


class UpdateNodeRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    draft_id: int
    json_path: str
    node_payload: dict


class ValidateRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    draft_id: int


class ActivateRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    draft_id: int


class GenerateRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    source_payload: dict


class GenerateFromExcelRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    file_path: str


class ExcelToJsonRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    file_path: str = "D:\\Mobifly2\\one_form_repo\\sample.xlsx"


class MigrateRootNodeRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    draft_id: int
    node_name: str


class BuildMissingNodesBundleRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    output_file: str = "D:\\Mobifly2\\one_form_repo\\missing_nodes_bundle.json"


class LoadMissingNodesBundleRequest(BaseModel):
    bundle_file: str = "D:\\Mobifly2\\one_form_repo\\missing_nodes_bundle.json"
    form_type: str = "ITR6_BASIC"
    actor: str = "bundle_loader"
    activate: bool = True


class ParityCheckRequest(BaseModel):
    excel_file_path: str
    form_type: str = "ITR6_BASIC"


class SyncFullLegacyRequest(BaseModel):
    form_type: str = "ITR6_BASIC"
    actor: str = "legacy_sync"
    activate: bool = True


app = FastAPI(title="One Form API", version="1.0.0")


def _ensure_output_table():
    with get_cursor() as (_, cur):
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS public.generated_payload (
                id BIGSERIAL PRIMARY KEY,
                form_type TEXT NOT NULL,
                structure_id BIGINT NOT NULL,
                version_major INT NOT NULL,
                version_minor INT NOT NULL,
                payload_json JSONB NOT NULL,
                generated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            )
            """
        )


def _persist_payload(payload: dict, form_type: str):
    active = form_type
    with get_cursor() as (_, cur):
        cur.execute(
            """
            SELECT id, version_major, version_minor
            FROM public.payload_structure
            WHERE form_type = %s AND is_active = TRUE
            ORDER BY version_major DESC, version_minor DESC
            LIMIT 1
            """,
            (active,),
        )
        row = cur.fetchone()
        if not row:
            raise ValueError("No active structure found")

        structure_id, vmaj, vmin = row
        cur.execute(
            """
            INSERT INTO public.generated_payload (
                form_type, structure_id, version_major, version_minor, payload_json
            )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
            """,
            (active, structure_id, vmaj, vmin, Json(payload)),
        )
        generated_id = cur.fetchone()[0]
        return generated_id, structure_id, vmaj, vmin


def _write_payload_file(payload: dict, generated_id: int):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_dir = os.path.join(base_dir, "outputs")
    os.makedirs(output_dir, exist_ok=True)

    latest_path = os.path.join(output_dir, "latest_payload.json")
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    archive_path = os.path.join(output_dir, f"payload_{generated_id}_{timestamp}.json")

    with open(latest_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    with open(archive_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    return latest_path, archive_path


@app.on_event("startup")
def startup_event():
    _ensure_output_table()


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/draft")
def create_draft(req: DraftRequest):
    try:
        api = OneFormServiceAPI(form_type=req.form_type, actor="api_user")
        draft_id = api.create_draft_from_active(req.next_major, req.next_minor)
        return {"draft_id": draft_id}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/node/update")
def update_node(req: UpdateNodeRequest):
    try:
        api = OneFormServiceAPI(form_type=req.form_type, actor="api_user")
        api.update_node(req.draft_id, req.json_path, req.node_payload)
        return {"updated": True, "draft_id": req.draft_id, "json_path": req.json_path}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/validate")
def validate(req: ValidateRequest):
    try:
        api = OneFormServiceAPI(form_type=req.form_type, actor="api_user")
        report = api.validate(req.draft_id)
        return report
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/activate")
def activate(req: ActivateRequest):
    try:
        api = OneFormServiceAPI(form_type=req.form_type, actor="api_user")
        api.activate(req.draft_id)
        return {"activated": True, "draft_id": req.draft_id}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/generate")
def generate(req: GenerateRequest):
    try:
        api = OneFormServiceAPI(form_type=req.form_type, actor="api_user")
        payload = api.generate(req.source_payload)
        generated_id, structure_id, vmaj, vmin = _persist_payload(payload, req.form_type)
        latest_path, archive_path = _write_payload_file(payload, generated_id)
        return {
            "generated_payload_id": generated_id,
            "form_type": req.form_type,
            "structure_id": structure_id,
            "version_major": vmaj,
            "version_minor": vmin,
            "saved_file_latest": latest_path,
            "saved_file_archive": archive_path,
            "payload": payload,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/generate-from-excel")
def generate_from_excel(req: GenerateFromExcelRequest):
    try:
        api = OneFormServiceAPI(form_type=req.form_type, actor="api_user")
        source_payload = parse_excel_to_source_payload(req.file_path)
        payload = api.generate(source_payload)
        generated_id, structure_id, vmaj, vmin = _persist_payload(payload, req.form_type)
        latest_path, archive_path = _write_payload_file(payload, generated_id)
        return {
            "generated_payload_id": generated_id,
            "form_type": req.form_type,
            "structure_id": structure_id,
            "version_major": vmaj,
            "version_minor": vmin,
            "excel_file_path": req.file_path,
            "saved_file_latest": latest_path,
            "saved_file_archive": archive_path,
            "source_payload_from_excel": source_payload,
            "payload": payload,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/excel-to-json")
def excel_to_json(req: ExcelToJsonRequest):
    """
    Single endpoint flow:
    Excel file -> source payload -> generated payload -> save JSON (DB + files).

    In ``legacy_exact`` mode, also runs legacy business validation
    (``buinsess_error_gen`` / ``business_error_on_file`` / ``priority_validation_first``)
    and returns those results alongside the payload.
    """
    try:
        api = OneFormServiceAPI(form_type=req.form_type, actor="api_user")
        mode = "legacy_exact"
        business_meta: dict = {
            "business_errors": [],
            "business_error_count": 0,
            "business_validation_status_failed": False,
        }
        try:
            legacy_exact = generate_legacy_exact_json(req.file_path)
            source_payload = legacy_exact["source_payload_from_excel"]
            payload = legacy_exact["payload"]
            business_meta = {
                "business_errors": legacy_exact.get("business_errors", []),
                "business_error_count": legacy_exact.get("business_error_count", 0),
                "business_validation_status_failed": legacy_exact.get(
                    "business_validation_status_failed", False
                ),
                "mat": legacy_exact.get("mat"),
                "matc": legacy_exact.get("matc"),
                "mat_removed": legacy_exact.get("mat_removed"),
                "legacy_business_response": legacy_exact.get("legacy_business_response"),
            }
            if legacy_exact.get("business_errors_skipped"):
                business_meta["business_errors_skipped"] = True
                business_meta["business_errors_skip_reason"] = legacy_exact.get(
                    "business_errors_skip_reason"
                )
        except Exception as exc:
            # Fallback for files without JSON_Config:
            # or when legacy-only dependencies are unavailable in runtime.
            source_payload = parse_excel_to_source_payload(req.file_path)
            payload = api.generate(source_payload)
            mode = f"fallback_source_payload ({str(exc)})"
            business_meta["business_validation_note"] = (
                "Legacy business validation was not run (fallback mode)."
            )

        generated_id, structure_id, vmaj, vmin = _persist_payload(payload, req.form_type)
        latest_path, archive_path = _write_payload_file(payload, generated_id)
        return {
            "message": "Excel processed successfully",
            "excel_file_path": req.file_path,
            "mode": mode,
            "generated_payload_id": generated_id,
            "form_type": req.form_type,
            "structure_id": structure_id,
            "version_major": vmaj,
            "version_minor": vmin,
            "saved_file_latest": latest_path,
            "saved_file_archive": archive_path,
            "payload": payload,
            **business_meta,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/migrate-root-node")
def migrate_root_node(req: MigrateRootNodeRequest):
    """
    One-by-one migration utility:
    loads one root node from legacy payload_config and updates it into a draft schema.
    """
    try:
        api = OneFormServiceAPI(form_type=req.form_type, actor="api_user")
        converted_node = load_legacy_root_node(req.node_name)
        api.update_node(req.draft_id, req.node_name, converted_node)
        return {
            "migrated": True,
            "draft_id": req.draft_id,
            "node_name": req.node_name,
            "note": "Run /validate and /activate after migrating required nodes.",
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/build-missing-nodes-bundle")
def build_missing_nodes(req: BuildMissingNodesBundleRequest):
    try:
        bundle = build_missing_nodes_bundle(
            form_type=req.form_type,
            output_file=req.output_file,
        )
        return {
            "built": True,
            "output_file": req.output_file,
            "missing_node_count": bundle.get("meta", {}).get("missing_node_count", 0),
            "note": "Load this file using src/load_missing_nodes_to_db.py",
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/load-missing-nodes-bundle")
def load_missing_nodes_bundle(req: LoadMissingNodesBundleRequest):
    try:
        with open(req.bundle_file, "r", encoding="utf-8") as f:
            bundle = json.load(f)

        nodes = bundle.get("nodes", {})
        rules = bundle.get("__rules__", {})

        api = OneFormServiceAPI(form_type=req.form_type, actor=req.actor)
        draft_id = api.create_draft_from_active()
        api.update_node(draft_id, "__rules__", rules)
        for node_name, node_def in nodes.items():
            api.update_node(draft_id, node_name, node_def)

        report = api.validate(draft_id)
        activated = False
        if req.activate and report.get("valid"):
            api.activate(draft_id)
            activated = True

        return {
            "loaded": True,
            "bundle_file": req.bundle_file,
            "draft_id": draft_id,
            "valid": report.get("valid"),
            "error_count": len(report.get("errors", [])),
            "errors_preview": report.get("errors", [])[:20],
            "activated": activated,
            "loaded_node_count": len(nodes),
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/parity-check")
def parity_check(req: ParityCheckRequest):
    try:
        result = compare_with_legacy(
            excel_file_path=req.excel_file_path,
            form_type=req.form_type,
        )
        return {
            "is_equal": result["is_equal"],
            "diff_count": result["diff_count"],
            "diffs_preview": result["diffs"][:50],
            "note": "Parity check compares outputs for the same source payload from excel_adapter.",
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/sync-full-legacy")
def sync_full_legacy(req: SyncFullLegacyRequest):
    """
    Full-fidelity sync:
    overwrite root nodes and rules from legacy payload_config into a new draft.
    """
    try:
        legacy_bundle = load_full_legacy_bundle()
        nodes = legacy_bundle.get("nodes", {})
        rules = legacy_bundle.get("__rules__", {})

        api = OneFormServiceAPI(form_type=req.form_type, actor=req.actor)
        draft_id = api.create_draft_from_active()
        api.update_node(draft_id, "__rules__", rules)

        for node_name, node_def in nodes.items():
            api.update_node(draft_id, node_name, node_def)

        report = api.validate(draft_id)
        activated = False
        if req.activate and report.get("valid"):
            api.activate(draft_id)
            activated = True

        return {
            "synced": True,
            "draft_id": draft_id,
            "root_node_count": len(nodes),
            "valid": report.get("valid"),
            "error_count": len(report.get("errors", [])),
            "errors_preview": report.get("errors", [])[:20],
            "activated": activated,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
