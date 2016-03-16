# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cp = head
        if cp == None or cp.next == None:
            return head
        np = cp.next
        cp.next = None
        while np:
            tmp = np
            np = np.next
            tmp.next = cp
            cp = tmp
        return cp