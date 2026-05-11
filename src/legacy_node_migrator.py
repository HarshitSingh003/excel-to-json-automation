from typing import Any

from .legacy_vendor import payload_config, transform_settings


TYPE_MAP = {
    "str": "str",
    "int": "int",
    "float": "float",
    "bool": "bool",
}


CAST_NAME_MAP = {
    "str_transform": "to_str",
    "int_transformation": "to_int",
    "float_transformation": "to_float",
    "float_transformation_without_roundof": "to_float",
    "bool_transformation": "to_str",
}


TRANSFORM_NAME_MAP = {
    "upper": "to_upper",
    "lower": "to_lower",
    "date_transform": "date_yyyy_mm_dd",
    "str_transform": "to_str",
    "int_transformation": "to_int",
    "float_transformation": "to_float",
    "float_transformation_without_roundof": "to_float",
}


def _callable_name(func_obj: Any) -> str | None:
    if func_obj is None:
        return None
    if hasattr(func_obj, "__name__"):
        return func_obj.__name__
    return str(func_obj)


def _python_type_to_name(type_obj: Any) -> str:
    if type_obj in (str, int, float, bool):
        return TYPE_MAP.get(type_obj.__name__, "str")
    type_name = getattr(type_obj, "__name__", "str")
    return TYPE_MAP.get(type_name, "str")


def _convert_field_tuple(field_tuple: tuple) -> dict:
    # Legacy tuple shape:
    # (name, type_obj, cast_func, allow_blank, transform_func, default_enabled, default_value)
    name = field_tuple[0]
    type_obj = field_tuple[1] if len(field_tuple) > 1 else str
    cast_func = field_tuple[2] if len(field_tuple) > 2 else None
    allow_blank = field_tuple[3] if len(field_tuple) > 3 else False
    transform_func = field_tuple[4] if len(field_tuple) > 4 else None
    default_enabled = bool(field_tuple[5]) if len(field_tuple) > 5 and field_tuple[5] else False
    default_value = field_tuple[6] if len(field_tuple) > 6 else None

    cast_name = CAST_NAME_MAP.get(_callable_name(cast_func), "to_str")
    transform_name = TRANSFORM_NAME_MAP.get(_callable_name(transform_func))

    return {
        "name": name,
        "type": _python_type_to_name(type_obj),
        "cast": cast_name,
        "allow_blank": bool(allow_blank),
        "transform": transform_name,
        "default_enabled": default_enabled,
        "default_value": default_value,
    }


def _convert_node(node_obj: dict) -> dict:
    converted = {}

    for field_key in ("field_required", "field_optional", "cm_field_map"):
        if field_key in node_obj and isinstance(node_obj[field_key], (list, tuple, set)):
            converted[field_key] = [
                _convert_field_tuple(item)
                for item in node_obj[field_key]
                if isinstance(item, tuple)
            ]

    for node_key in ("node_required", "node_optional", "array_required", "array_optional"):
        if node_key in node_obj and isinstance(node_obj[node_key], dict):
            converted[node_key] = {}
            for child_name, child_node in node_obj[node_key].items():
                # Legacy configs sometimes nest field collections under node maps.
                # Promote them to current node-level fields for compatibility.
                if child_name in ("field_required", "field_optional", "cm_field_map") and isinstance(
                    child_node, (list, tuple, set)
                ):
                    converted_fields = [
                        _convert_field_tuple(item) for item in child_node if isinstance(item, tuple)
                    ]
                    converted[child_name] = converted_fields
                    # Preserve legacy odd shape too (field_* inside node maps)
                    # as a no-op child node for full-fidelity structure parity.
                    converted[node_key][child_name] = {child_name: converted_fields}
                    continue
                if isinstance(child_node, dict):
                    converted[node_key][child_name] = _convert_node(child_node)

    if "cm_node_map" in node_obj and isinstance(node_obj["cm_node_map"], dict):
        converted["cm_node_map"] = {}
        for child_name, child_node in node_obj["cm_node_map"].items():
            if isinstance(child_node, dict):
                converted["cm_node_map"][child_name] = _convert_node(child_node)

    return converted


def load_legacy_root_node(node_name: str) -> dict:
    structure = getattr(payload_config, "MANDATORY_NODE_STRUCTURE", {})
    if node_name not in structure:
        raise ValueError(f"Root node '{node_name}' not found in legacy payload_config")

    root_node = structure[node_name]
    if not isinstance(root_node, dict):
        raise ValueError(f"Root node '{node_name}' is not a node object")

    return _convert_node(root_node)


def load_full_legacy_bundle() -> dict:
    legacy_structure = getattr(payload_config, "MANDATORY_NODE_STRUCTURE", {})
    check_def_and_set = getattr(transform_settings, "CHECK_DEF_AND_SET", [])

    converted_nodes = {}
    for root_name, root_node in legacy_structure.items():
        if isinstance(root_node, dict):
            converted_nodes[root_name] = _convert_node(root_node)

    return {
        "__rules__": {
            "check_def_and_set": list(check_def_and_set),
        },
        "nodes": converted_nodes,
    }
