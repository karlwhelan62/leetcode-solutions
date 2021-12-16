import unittest
from src.search_insert import Solution

class TestSolution(unittest.TestCase):

    def test_search_insert(self):
        test_object = Solution()
        self.assertEqual(test_object.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(test_object.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(test_object.searchInsert([1, 3, 5, 6], 7), 4)
