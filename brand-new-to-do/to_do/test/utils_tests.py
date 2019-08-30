""" Tests for utils.py"""

import unittest


from ..utils import match_state, unmatch_state
from ..constant import UI, NUNI


class TestMatchState(unittest.TestCase):

    def test_match_state(self):
        test_data = {"is_urgent": 0, "is_important": 0}
        expected_result = {"state": NUNI}
        actual_result = match_state(test_data)
        self.assertEqual(expected_result, actual_result)


class TestUnMatchState(unittest.TestCase):

    def test_un_match_state(self):
        state = UI
        expected_result = {"is_urgent": 1, "is_important": 1}
        actual_result = unmatch_state(state)
        self.assertEqual(expected_result, actual_result)
