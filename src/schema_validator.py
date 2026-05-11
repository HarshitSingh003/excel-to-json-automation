from jsonschema import Draft7Validator

from .transform_registry import CAST_REGISTRY, TRANSFORM_REGISTRY


FIELD_SCHEMA = {
    "type": "object",
    "required": [
        "name",
        "type",
        "cast",
        "allow_blank",
        "transform",
        "default_enabled",
        "default_value",
    ],
    "additionalProperties": False,
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "type": {"type": "string", "minLength": 1},
        "cast": {"type": "string", "minLength": 1},
        "allow_blank": {"type": "boolean"},
        "transform": {"type": ["string", "null"]},
        "default_enabled": {"type": "boolean"},
        "default_value": {},
    },
}


NODE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "field_required": {"type": "array", "items": FIELD_SCHEMA},
        "field_optional": {"type": "array", "items": FIELD_SCHEMA},
        "cm_field_map": {"type": "array", "items": FIELD_SCHEMA},
        "cm_node_map": {"type": "object"},
        "node_required": {"type": "object"},
        "node_optional": {"type": "object"},
        "array_required": {"type": "object"},
        "array_optional": {"type": "object"},
    },
}


def _walk_node(node, errors, prefix="$"):
    for key in (
        "node_required",
        "node_optional",
        "array_required",
        "array_optional",
        "cm_node_map",
    ):
        child_map = node.get(key, {})
        if isinstance(child_map, dict):
            for child_name, child_node in child_map.items():
                if not isinstance(child_node, dict):
                    errors.append(f"{prefix}.{key}.{child_name} must be an object")
                    continue
                _walk_node(child_node, errors, f"{prefix}.{key}.{child_name}")

    for key in ("field_required", "field_optional", "cm_field_map"):
        field_list = node.get(key, [])
        for idx, field_def in enumerate(field_list):
            if field_def["cast"] not in CAST_REGISTRY:
                errors.append(f"{prefix}.{key}[{idx}] cast '{field_def['cast']}' not found")

            transform_name = field_def.get("transform")
            if transform_name and transform_name not in TRANSFORM_REGISTRY:
                errors.append(
                    f"{prefix}.{key}[{idx}] transform '{transform_name}' not found"
                )


def validate_structure(schema_json):
    errors = []

    if not isinstance(schema_json, dict):
        return {"valid": False, "errors": ["Root schema must be an object"]}

    rules = schema_json.get("__rules__", {})
    if rules and not isinstance(rules, dict):
        errors.append("__rules__ must be an object")
    if isinstance(rules, dict):
        check_def = rules.get("check_def_and_set", [])
        if check_def and not (
            isinstance(check_def, list) and all(isinstance(x, str) for x in check_def)
        ):
            errors.append("__rules__.check_def_and_set must be list[str]")

    for root_name, root_node in schema_json.items():
        if root_name == "__rules__":
            continue
        validator = Draft7Validator(NODE_SCHEMA)
        root_errors = sorted(validator.iter_errors(root_node), key=lambda e: e.path)
        for err in root_errors:
            errors.append(f"{root_name}: {err.message}")
        if isinstance(root_node, dict):
            _walk_node(root_node, errors, prefix=f"$.{root_name}")

    return {"valid": len(errors) == 0, "errors": errors}
