import unittest
from src.valid_parentheses import Solution

class TestSolution(unittest.TestCase):

    def test_valid_parentheses(self):
        test_object = Solution()
        self.assertTrue(test_object.isValid("()"))
        self.assertTrue(test_object.isValid("()[]{}"))
        self.assertFalse(test_object.isValid("(]"))
        self.assertFalse(test_object.isValid("([)]"))
        self.assertTrue(test_object.isValid("{[]}"))
        self.assertTrue(test_object.isValid("{[({[]})]}"))
