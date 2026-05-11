"""
Run excelToJson business validation on a final ITR6 payload + workbook.

Delegates to the legacy ``payload_generator.GeneratePayload`` implementation
(``buinsess_error_gen``, ``business_error_on_file``, ``priority_validation_first``)
so all rules in ``business_configuration`` / ``business_validation`` stay identical.
"""

from __future__ import annotations

from typing import Any

from .legacy_exact_from_file import _ensure_crypto_stub


def run_legacy_business_error_pipeline(
    final_payload: dict[str, Any],
    workbook,
    mat: bool,
    matc: bool,
) -> dict[str, Any]:
    """
    Mirror ``exceltojson.parse_excel_to_json`` after ``parent_gen_payload``:

    - ``GeneratePayload.buinsess_error_gen(payload, response)``
    - ``GeneratePayload.business_error_on_file(payload, response, workbook)``
    - If ``mat`` or ``matc``: filter errors with ``lists.mat_business_pass``, then
      ``priority_validation_first``; else ``priority_validation_first`` on full lists.

    ``final_payload`` must be ``{"ITR": {"ITR6": ...}}`` (post-``parent_gen_payload``),
    matching the object passed to those methods in the legacy service.
    """
    _ensure_crypto_stub()
    from .legacy_vendor import lists as lists_mod
    from .legacy_vendor import payload_generator as payload_generator_mod

    GeneratePayload = payload_generator_mod.GeneratePayload
    mat_business_pass = lists_mod.mat_business_pass

    response: dict[str, Any] = {"json_error": {}, "status": True}
    b_val_1 = GeneratePayload.buinsess_error_gen(final_payload, response)
    b_val_2 = GeneratePayload.business_error_on_file(final_payload, response, workbook)

    if mat or matc:
        mat_val1 = [val for val in b_val_1 if val["name_range"] not in mat_business_pass]
        mat_val2 = [val for val in b_val_2 if val["name_range"] not in mat_business_pass]
        GeneratePayload.priority_validation_first(response, mat_val1, mat_val2)
    else:
        GeneratePayload.priority_validation_first(response, b_val_1, b_val_2)

    business_errors = response.get("json_error", {}).get("business_errors", [])
    return {
        "business_errors": business_errors,
        "business_error_count": len(business_errors),
        "business_validation_status_failed": not response.get("status", True),
        "legacy_business_response": {
            "json_error": response.get("json_error", {}),
            "status": response.get("status", True),
        },
    }
