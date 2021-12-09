import unittest
from src.longest_common_prefix import Solution

class TestSolution(unittest.TestCase):

    def test_longest_common_prefix(self):
        test_object = Solution()
        self.assertEqual(test_object.longestCommonPrefix(['flower', 
                                                           'flow', 
                                                           'flight']),
                        'fl')
        self.assertEqual(test_object.longestCommonPrefix(['dog', 
                                                          'racecar', 
                                                          'car']),
                        '')
        self.assertEqual(test_object.longestCommonPrefix(['connive', 
                                                          'convince', 
                                                          'conceive',
                                                          'convex']),
                        'con')
        self.assertEqual(test_object.longestCommonPrefix(['interpret', 
                                                          'interview', 
                                                          'intermingle',
                                                          'intervene']),
                        'inter')
        self.assertEqual(test_object.longestCommonPrefix(['dip', 
                                                          'dive', 
                                                          'duck',
                                                          'dodge']),
                        'd')
        self.assertEqual(test_object.longestCommonPrefix(['home', 
                                                          'home', 
                                                          'home']),
                        'home')
