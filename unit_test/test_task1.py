"""
Tests for assignment1 and task1.
"""

import unittest

import task1


class StringManipulationTest(unittest.TestCase):
    """
    Tests for string manipulation task.
    """
    def test_remove_all_except_first(self):
        """
        Test that all character in a strings are removed except first character
        """
        argument_and_expected_result = {
            "a": "a",
            "aa": "a",
            "aaa": "a",
            "aba": "ab",
            "bba": "ba",
            "aab": "ab",
            "TechCity": "Techiy",
        }
        for word, expected_result in argument_and_expected_result.items():
            result = task1.remove_all_except_first(word)
            self.assertEqual(result, expected_result)

    def test_remove_first_occurrence(self):
        """
        Test that first occurrence of character is removed in a string
        """
        argument_and_expected_result = {
            "a": "a",
            "aa": "a",
            "aaa": "aa",
            "aba": "ba",
            "bba": "ba",
            "aab": "ab",
            "TechTeam": "chTeam",
        }
        for word, expected_result in argument_and_expected_result.items():
            result = task1.remove_first_occurrence(word)
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
