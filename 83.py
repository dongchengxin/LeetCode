# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cp = head
        if not cp:
            return head
        while cp.next:
            if cp.next.val == cp.val:
                cp.next = cp.next.next
            else:
                cp = cp.next
        return head