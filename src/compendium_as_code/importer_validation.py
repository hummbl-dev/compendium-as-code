"""Importer fixture validation helpers for compendium-as-code.

These checks intentionally operate on synthetic fixture records and are not a full
Compendium parser. They enforce source-boundary invariants that the adapter
contracts rely on.
"""

from __future__ import annotations

from pathlib import Path
from typing import Mapping, MutableMapping, Sequence

import json

from .met import assert_met_unchanged
from .normalize import normalize_activity_code
from .validate import require_upstream_met_source

_UPSTREAM_ACTIVITY_KEYS = {"activity_code", "activity_description", "met", "met_source"}
_ALLOWED_IMPORTER_KEYS = frozenset(
    {
        "activity_code",
        "activity_description",
        "met",
        "met_source",
        "hummbl_annotations",
    }
)


def load_importer_fixture(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def validate_importer_fixture(fixture: Mapping[str, object]) -> None:
    source = fixture["source_activity"]
    imported = fixture["imported_activity"]
    if not isinstance(source, Mapping) or not isinstance(imported, Mapping):
        raise ValueError("Fixture source/imported payloads must be mapping objects.")

    _validate_activity_preservation(source, imported)
    require_upstream_met_source(imported)
    _validate_separate_annotations(imported)

    if fixture.get("relationship", "same") == "merged":
        _validate_merged_met_levels(fixture)


def _validate_activity_preservation(source: Mapping[str, object], imported: Mapping[str, object]) -> None:
    source_code = normalize_activity_code(str(source["activity_code"]))
    imported_code = normalize_activity_code(str(imported["activity_code"]))
    if source_code != imported_code:
        raise ValueError("Imported activity code must match source activity code after normalization.")

    if source["activity_description"] != imported["activity_description"]:
        raise ValueError("Imported activity description must preserve source activity description.")

    source_met = float(source["met"])
    imported_met = float(imported["met"])
    assert_met_unchanged(source_met, imported_met)


def _validate_merged_met_levels(fixture: Mapping[str, object]) -> None:
    source_rows = fixture["source_activities"]
    imported = fixture["imported_activity"]
    if not isinstance(source_rows, Sequence) or len(source_rows) < 2:
        raise ValueError("Merged relationship requires at least two source activities.")

    met_values = {_normalize_met(row["met"]) for row in source_rows}
    if len(met_values) != 1:
        raise ValueError(
            "Cannot merge activities with different MET levels."
        )

    assert_met_unchanged(next(iter(met_values)), float(imported["met"]))


def _validate_separate_annotations(imported: Mapping[str, object]) -> None:
    if not isinstance(imported, MutableMapping):
        raise ValueError("Imported activity record must be a mutable mapping.")

    annotation_payload = imported.get("hummbl_annotations")
    if not isinstance(annotation_payload, Mapping):
        raise ValueError("Imported activities must include hummbl_annotations as a mapping.")

    extra_top_level_keys = set(imported.keys()) - _ALLOWED_IMPORTER_KEYS
    if extra_top_level_keys:
        raise ValueError(
            "All HUMMBL-derived fields must be nested under hummbl_annotations."
        )

    if any(k in _UPSTREAM_ACTIVITY_KEYS for k in annotation_payload):
        raise ValueError("HUMMBL annotations must not reuse upstream activity field names.")


def _normalize_met(value: object) -> float:
    return float(value)
