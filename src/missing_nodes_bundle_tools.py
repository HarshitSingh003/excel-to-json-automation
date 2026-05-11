import json

from .legacy_node_migrator import load_full_legacy_bundle
from .structure_service import get_active_structure


def build_missing_nodes_bundle(
    form_type: str,
    output_file: str,
):
    legacy_bundle = load_full_legacy_bundle()
    legacy_nodes = legacy_bundle["nodes"]
    rules = legacy_bundle.get("__rules__", {})

    active = get_active_structure(form_type)
    active_schema = active["schema_json"]
    active_root_keys = {k for k in active_schema.keys() if k != "__rules__"}

    missing = {k: v for k, v in legacy_nodes.items() if k not in active_root_keys}
    bundle = {
        "__rules__": rules,
        "nodes": missing,
        "meta": {
            "form_type": form_type,
            "missing_node_count": len(missing),
            "source": "legacy_payload_config",
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2)

    return bundle
