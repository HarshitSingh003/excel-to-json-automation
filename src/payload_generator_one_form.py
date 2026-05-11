from .transform_registry import CAST_REGISTRY, TRANSFORM_REGISTRY


def _has_value(value):
    # Legacy-compatible truthy check:
    # values like 0/False/"" are treated as blank unless allow_blank/default applies.
    return bool(value)


def _process_fields(field_defs, source_data, output):
    for field in field_defs:
        name = field["name"]
        expected_type_name = field["type"]
        cast_name = field["cast"]
        allow_blank = field["allow_blank"]
        transform_name = field["transform"]
        default_enabled = field["default_enabled"]
        default_value = field["default_value"]

        if name in source_data:
            value = source_data[name]
            if _has_value(value):
                expected_type = CAST_REGISTRY[expected_type_name]
                if not isinstance(value, expected_type):
                    value = CAST_REGISTRY[cast_name](value)
                if transform_name:
                    value = TRANSFORM_REGISTRY[transform_name](value)
                output[name] = value
            elif allow_blank:
                output[name] = value
            elif default_enabled:
                output[name] = default_value
        elif default_enabled:
            output[name] = default_value


def _process_cm_fields(cm_field_defs, source_data, output, check_def_and_set):
    for field in cm_field_defs:
        name = field["name"]
        expected_type_name = field["type"]
        cast_name = field["cast"]
        allow_blank = field["allow_blank"]
        default_enabled = field["default_enabled"]
        default_value = field["default_value"]
        transform_name = field.get("transform")

        if name not in output and name in source_data:
            value = source_data[name]
            if _has_value(value):
                expected_type = CAST_REGISTRY.get(expected_type_name, str)
                if not isinstance(value, expected_type):
                    value = CAST_REGISTRY[cast_name](value)
                if transform_name:
                    value = TRANSFORM_REGISTRY[transform_name](value)
                output[name] = value
            elif allow_blank:
                output[name] = value
            elif default_enabled:
                output[name] = default_value
        elif (
            name in check_def_and_set
            and name not in output
            and name not in source_data
            and default_enabled
        ):
            output[name] = default_value


def _collect_modeled_keys(node_def):
    keys = set()
    for field_group in ("field_required", "field_optional", "cm_field_map"):
        for field in node_def.get(field_group, []):
            name = field.get("name")
            if name:
                keys.add(name)
    for group in ("node_required", "node_optional", "array_required", "array_optional", "cm_node_map"):
        keys.update(node_def.get(group, {}).keys())
    return keys


def _copy_unmodeled_scalar_fields(node_def, source_data, output, rules):
    # Dynamic mode: preserve scalar fields not declared in schema so newly added
    # Excel mappings (e.g. custom address/email nodes) are not silently dropped.
    if not rules.get("preserve_unmodeled_scalars", True):
        return
    modeled_keys = _collect_modeled_keys(node_def)
    for key, value in source_data.items():
        if key in output or key in modeled_keys:
            continue
        if isinstance(value, (dict, list, tuple, set)):
            continue
        output[key] = value


def _generate_node(node_def, source_data, rules):
    if not isinstance(source_data, dict):
        return {}

    out = {}
    check_def_and_set = rules.get("check_def_and_set", [])

    _process_fields(node_def.get("field_required", []), source_data, out)
    _process_fields(node_def.get("field_optional", []), source_data, out)

    for child_name, child_def in node_def.get("node_required", {}).items():
        if child_name in source_data:
            child = _generate_node(child_def, source_data[child_name], rules)
            if child:
                out[child_name] = child

    for child_name, child_def in node_def.get("node_optional", {}).items():
        if child_name in source_data:
            child = _generate_node(child_def, source_data[child_name], rules)
            if child:
                out[child_name] = child

    for arr_name, arr_node_def in node_def.get("array_required", {}).items():
        if arr_name in source_data and isinstance(source_data[arr_name], list):
            arr = []
            for item in source_data[arr_name]:
                child = _generate_node(arr_node_def, item, rules)
                if child:
                    arr.append(child)
            if arr:
                out[arr_name] = arr

    for arr_name, arr_node_def in node_def.get("array_optional", {}).items():
        if arr_name in source_data and isinstance(source_data[arr_name], list):
            arr = []
            for item in source_data[arr_name]:
                child = _generate_node(arr_node_def, item, rules)
                if child:
                    arr.append(child)
            if arr:
                out[arr_name] = arr

    # Legacy-compatible cm_field_map behavior runs only if node already has content.
    if node_def.get("cm_field_map") and out:
        _process_cm_fields(node_def.get("cm_field_map", []), source_data, out, check_def_and_set)

    # Legacy-compatible cm_node_map behavior runs only if node already has content.
    if node_def.get("cm_node_map") and out:
        for cm_node_key, cm_node_value in node_def.get("cm_node_map", {}).items():
            if cm_node_key not in out and cm_node_key in source_data:
                cm_node = _generate_node(cm_node_value, source_data[cm_node_key], rules)
                if cm_node:
                    out[cm_node_key] = cm_node

    _copy_unmodeled_scalar_fields(node_def, source_data, out, rules)

    return out


def generate_payload(schema_json, source_payload):
    final_payload = {}
    rules = schema_json.get("__rules__", {})
    for root_key, root_def in schema_json.items():
        if root_key == "__rules__":
            continue
        if root_key in source_payload:
            node = _generate_node(root_def, source_payload[root_key], rules)
            if node:
                final_payload[root_key] = node
    return final_payload
