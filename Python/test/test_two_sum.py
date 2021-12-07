import unittest
from src.two_sum import Solution

class TestSolution(unittest.TestCase):

    def test_twoSum(self):
        test_object = Solution()
        self.assertEqual(test_object.twoSum([2, 7, 11, 15], 9),
                        [0, 1])
        self.assertEqual(test_object.twoSum([3, 2, 4], 6),
                        [1, 2])
        self.assertEqual(test_object.twoSum([3, 3], 6),
                        [0, 1])
