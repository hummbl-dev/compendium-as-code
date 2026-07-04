import unittest

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "src"))

from compendium_as_code.normalize import normalize_activity_code


class ActivityCodeFormatTests(unittest.TestCase):
    def test_activity_code_is_trimmed_not_rewritten(self):
        self.assertEqual(normalize_activity_code(" 12345 "), "12345")
