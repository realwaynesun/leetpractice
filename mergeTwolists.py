class ListNode:
    def __init__(self, x=0, next=None):
        self.x = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        dummy = ListNode()
        c = dummy
        while list1 and list2:
            if list1.x <= list2.x:
                c.next = list1
                list1 = list1.next
            else:
                c.next = list2
                list2 = list2.next
            c = c.next
        c.next = list1 or list2
        return dummy.next