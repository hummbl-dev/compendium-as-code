import unittest

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "src"))


class HeadingConsistencyTests(unittest.TestCase):
    def test_heading_consistency_placeholder(self):
        self.assertTrue(True)
