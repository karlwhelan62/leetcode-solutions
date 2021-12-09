import unittest
from src.palindrome_number import Solution

class TestSolution(unittest.TestCase):

    def test_palindrome_number(self):
        test_object = Solution()
        self.assertTrue(test_object.isPalindrom(121))
        self.assertFalse(test_object.isPalindrom(-121))
        self.assertTrue(test_object.isPalindrom(4567654))
        self.assertFalse(test_object.isPalindrom(-101))
        self.assertFalse(test_object.isPalindrom(10))
