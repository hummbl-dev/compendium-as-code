"""MET semantics helpers."""


def assert_met_unchanged(original: float, imported: float) -> None:
    if original != imported:
        raise ValueError("Upstream MET values must not be changed during import.")
