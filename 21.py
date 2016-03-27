# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        p = l
        while l1 or l2:
            if l1 and (not l2 or l1.val < l2.val):
                l.next = ListNode(l1.val)
                l1 = l1.next
            elif not l1 or l1.val >= l2.val:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next
        return p.next