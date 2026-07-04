import json
import unittest
from pathlib import Path


class SchemaValidityTests(unittest.TestCase):
    def test_schema_files_parse_as_json(self):
        for path in Path("schemas").glob("*.json"):
            json.loads(path.read_text(encoding="utf-8"))
