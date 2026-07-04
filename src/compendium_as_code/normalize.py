"""Normalization helpers that preserve upstream source values."""


def normalize_activity_code(value: str) -> str:
    return value.strip()
