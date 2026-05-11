from datetime import datetime


def to_str(value):
    return str(value).strip()


def to_int(value):
    return int(value)


def to_float(value):
    return float(value)


def to_upper(value):
    return str(value).upper()


def to_lower(value):
    return str(value).lower()


def date_yyyy_mm_dd(value):
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d")
    return str(value)


CAST_REGISTRY = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    # Alias keys to support object schemas using cast function names.
    "to_str": to_str,
    "to_int": to_int,
    "to_float": to_float,
}

TRANSFORM_REGISTRY = {
    "to_str": to_str,
    "to_int": to_int,
    "to_float": to_float,
    "to_upper": to_upper,
    "to_lower": to_lower,
    "date_yyyy_mm_dd": date_yyyy_mm_dd,
}
