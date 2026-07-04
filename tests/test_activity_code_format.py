import unittest

from compendium_as_code.normalize import normalize_activity_code


class ActivityCodeFormatTests(unittest.TestCase):
    def test_activity_code_is_trimmed_not_rewritten(self):
        self.assertEqual(normalize_activity_code(" 12345 "), "12345")
