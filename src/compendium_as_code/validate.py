"""Validation helpers for Compendium adapter records."""


def require_upstream_met_source(record: dict) -> None:
    if record.get("met_source") != "upstream":
        raise ValueError("Compendium MET values must be marked as upstream unless explicitly derived.")
