# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cp = head
        np = cp.next
        head = np
        while cp:
            tmp = np.next
            np.next = cp
            if tmp and tmp.next:
                cp.next = tmp.next
                cp = tmp
                np = tmp.next
            else:
                cp.next = tmp
                break
        return head