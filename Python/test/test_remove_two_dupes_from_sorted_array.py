import unittest
from src.remove_dupes_from_sorted_array import Solution

class TestSolution(unittest.TestCase):

    def test_remove_dupes_from_sorted_array(self):
        test_object = Solution()
        self.assertEqual(test_object.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(test_object.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(test_object.removeDuplicates([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6]), 7)
