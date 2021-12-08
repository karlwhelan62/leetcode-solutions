import unittest
from src.roman_to_integer import Solution

class TestSolution(unittest.TestCase):

    def test_roman_to_int(self):
        test_object = Solution()
        self.assertEqual(test_object.romainToInt("III"), 3)
        self.assertEqual(test_object.romainToInt("IV"), 4)
        self.assertEqual(test_object.romainToInt("IX"), 9)
        self.assertEqual(test_object.romainToInt("LVIII"), 58)
        self.assertEqual(test_object.romainToInt("MCMXCIV"), 1994)
        self.assertEqual(test_object.romainToInt("MCMXCVIII"), 1998)
        self.assertEqual(test_object.romainToInt("MMXXI"), 2021)