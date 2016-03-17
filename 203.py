# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None and head.val == val:
            head = head.next
        cp = head
        if cp == None or cp.next == None:
            return head
        while cp.next:
            if cp.next.val == val:
                cp.next = cp.next.next
            else:
                cp = cp.next
        return head