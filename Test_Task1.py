import unittest
import Task1

class StringManipulation(unittest.TestCase):
    def test_removeAllExceptFirst(self):
        result = Task1.removeAllExceptFirst("TechCity")
        self.assertEqual(result, "Techiy")

    def test_removeFirstOccurrence(self):
        result = Task1.removeFirstOccurrence("TechTeam")
        self.assertEqual(result, "chTeam")


if __name__ == '__main__':
    unittest.main()
