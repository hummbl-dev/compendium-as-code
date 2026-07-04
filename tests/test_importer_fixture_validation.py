import unittest
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "src"))

from compendium_as_code.importer_validation import (
    load_importer_fixture,
    validate_importer_fixture,
)


class ImporterFixtureValidationTests(unittest.TestCase):
    fixtures_dir = Path(__file__).resolve().parent / "fixtures"

    def test_adult_importer_fixture_is_valid(self):
        fixture = load_importer_fixture(self.fixtures_dir / "adult_2024.importer.fixture.json")
        validate_importer_fixture(fixture)

    def test_older_adult_importer_fixture_is_valid(self):
        fixture = load_importer_fixture(
            self.fixtures_dir / "older_adult_2024.importer.fixture.json"
        )
        validate_importer_fixture(fixture)

    def test_wheelchair_importer_fixture_is_valid(self):
        fixture = load_importer_fixture(
            self.fixtures_dir / "wheelchair_2024.importer.fixture.json"
        )
        validate_importer_fixture(fixture)

    def test_importer_rejects_changed_met_value(self):
        fixture = load_importer_fixture(
            self.fixtures_dir / "adult_2024.met_change_rejection.fixture.json"
        )
        with self.assertRaises(ValueError):
            validate_importer_fixture(fixture)

    def test_importer_rejects_merged_activities_with_conflicting_mets(self):
        fixture = load_importer_fixture(
            self.fixtures_dir / "merged_met_conflict.importer.fixture.json"
        )
        with self.assertRaises(ValueError):
            validate_importer_fixture(fixture)

    def test_hummbl_annotations_are_nested(self):
        fixture = load_importer_fixture(self.fixtures_dir / "adult_2024.importer.fixture.json")
        fixture["imported_activity"]["activity_origin"] = "derived"
        with self.assertRaises(ValueError):
            validate_importer_fixture(fixture)
