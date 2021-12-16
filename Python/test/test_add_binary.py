import unittest
from src.add_binary import Solution

class TestSolution(unittest.TestCase):

    def test_add_binary(self):
        test_object = Solution()
        self.assertEqual(test_object.addBinary("11", "1"), "100")
        self.assertEqual(test_object.addBinary("1010", "1011"), "10101")
