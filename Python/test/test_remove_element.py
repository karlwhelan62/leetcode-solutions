import unittest
from src.remove_element import Solution

class TestSolution(unittest.TestCase):

    def test_remove_element(self):
        test_object = Solution()
        self.assertEqual(test_object.removeElement([3, 2, 2, 3], 3), 2)
        self.assertEqual(test_object.removeElement([0,1,2,2,3,0,4,2], 2), 5)
        self.assertEqual(test_object.removeElement([1], 1), 0)
        self.assertEqual(test_object.removeElement([1, 1, 1, 1, 1], 1), 0)
