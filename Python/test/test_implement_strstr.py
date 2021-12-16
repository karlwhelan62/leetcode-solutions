import unittest
from src.implement_strstr import Solution

class TestSolution(unittest.TestCase):

    def test_implement_strstr(self):
        test_object = Solution()
        self.assertEqual(test_object.strStr("hello", "ll"), 2)
        self.assertEqual(test_object.strStr("aaaaa", "bba"), -1)
        self.assertEqual(test_object.strStr("", ""), 0)
        self.assertEqual(test_object.strStr("a", "a"), 0)
