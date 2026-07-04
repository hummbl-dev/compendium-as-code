import unittest

from compendium_as_code.met import assert_met_unchanged


class MetValueTests(unittest.TestCase):
    def test_met_value_change_is_rejected(self):
        with self.assertRaises(ValueError):
            assert_met_unchanged(3.5, 3.6)
