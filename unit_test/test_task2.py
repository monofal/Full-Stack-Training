"""
Tests for assignment1 and task2.
"""

import unittest

from basic_data_types import task2


class MultiplyDigitTest(unittest.TestCase):
    """
    Tests for task multiply digits of a string.
    """
    def test_multiply(self):
        """
        Test that returned value is product of digits.
        """
        argument_and_expected_result = {
            111: 1,
            121: 2,
            444: 64,
            153: 15,
        }
        for word, expected_result in argument_and_expected_result.items():
            result = task2.multiply_digits_of_number(word)
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
