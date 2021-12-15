import unittest
from src.linked_list import LinkedList
from src.merge_two_sorted_lists import Solution

class TestSolution(unittest.TestCase):

    def test_merge_two_lists(self):
        test_object = Solution()
        List1 = [1, 2, 4]
        list2 = [1, 3, 4]
        ll1 = LinkedList(List1)
        ll2 = LinkedList(list2)
        ll3 = test_object.mergeTwoLists(ll1.head, ll2.head)
        self.assertEqual(ll3.convertToArray(), [1, 1, 2, 3, 4, 4])

        List1 = []
        list2 = []
        ll1 = LinkedList(List1)
        ll2 = LinkedList(list2)
        ll3 = test_object.mergeTwoLists(ll1.head, ll2.head)
        self.assertEqual(ll3, [])

        List1 = []
        list2 = [0]
        ll1 = LinkedList(List1)
        ll2 = LinkedList(list2)
        ll3 = test_object.mergeTwoLists(ll1.head, ll2.head)
        self.assertEqual(ll3.convertToArray(), [0])

    def test_merge_two_lists_recur(self):
        test_object = Solution()
        List1 = [1, 2, 4]
        list2 = [1, 3, 4]
        ll1 = LinkedList(List1)
        ll2 = LinkedList(list2)
        ll3 = test_object.mergeTwoLists(ll1.head, ll2.head)
        self.assertEqual(ll3.convertToArray(), [1, 1, 2, 3, 4, 4])

        List1 = []
        list2 = []
        ll1 = LinkedList(List1)
        ll2 = LinkedList(list2)
        ll3 = test_object.mergeTwoLists(ll1.head, ll2.head)
        self.assertEqual(ll3, [])

        List1 = []
        list2 = [0]
        ll1 = LinkedList(List1)
        ll2 = LinkedList(list2)
        ll3 = test_object.mergeTwoLists(ll1.head, ll2.head)
        self.assertEqual(ll3.convertToArray(), [0])
