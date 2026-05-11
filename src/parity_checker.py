import json
from typing import Any

from .excel_adapter import parse_excel_to_source_payload
from .legacy_exact_from_file import _ensure_crypto_stub
from .service_api import OneFormServiceAPI


def _collect_differences(a: Any, b: Any, path: str, diffs: list[str]):
    if type(a) is not type(b):
        diffs.append(f"{path}: type mismatch ({type(a).__name__} vs {type(b).__name__})")
        return

    if isinstance(a, dict):
        keys = set(a.keys()) | set(b.keys())
        for key in sorted(keys):
            if key not in a:
                diffs.append(f"{path}.{key}: missing in one_form_repo")
                continue
            if key not in b:
                diffs.append(f"{path}.{key}: missing in legacy")
                continue
            _collect_differences(a[key], b[key], f"{path}.{key}", diffs)
        return

    if isinstance(a, list):
        if len(a) != len(b):
            diffs.append(f"{path}: list length mismatch ({len(a)} vs {len(b)})")
            return
        for idx, (av, bv) in enumerate(zip(a, b)):
            _collect_differences(av, bv, f"{path}[{idx}]", diffs)
        return

    if a != b:
        diffs.append(f"{path}: value mismatch ({json.dumps(a)} vs {json.dumps(b)})")


def compare_with_legacy(excel_file_path: str, form_type: str = "ITR6_BASIC"):
    _ensure_crypto_stub()
    from .legacy_vendor.payload_generator import GeneratePayload

    source_payload = parse_excel_to_source_payload(excel_file_path)

    api = OneFormServiceAPI(form_type=form_type, actor="parity_checker")
    one_form_payload = api.generate(source_payload)

    legacy_payload = GeneratePayload.parent_gen_payload(source_payload)

    diffs: list[str] = []
    _collect_differences(one_form_payload, legacy_payload, "$", diffs)
    return {
        "is_equal": len(diffs) == 0,
        "diff_count": len(diffs),
        "diffs": diffs[:200],
        "source_payload": source_payload,
        "one_form_payload": one_form_payload,
        "legacy_payload": legacy_payload,
    }
