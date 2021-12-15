class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def convertToArray(self):
        array = []
        current = self
        while current.next:
            array.append(current.val)
            current = current.next

        array.append(current.val)
        return array


class LinkedList:

    def __init__(self, lst=None):
        if not lst:
            self.head = []
        else:    
            self.head = ListNode(lst[0])
            current = self.head
            for item in lst[1:]:
                current.next = ListNode(item)
                current = current.next

