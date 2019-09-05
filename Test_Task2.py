import Task2
import unittest


class MultiplyDigit(unittest.TestCase):
    def test_multiply(self):
        result = Task2.multiplyDigitsOfNumber(1234)
        self.assertEqual(result, 24)


if __name__ == '__main__':
    unittest.main()