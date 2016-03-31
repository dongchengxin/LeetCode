# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cp = head
        np = cp
        l = 0
        while np:
            l += 1
            np = np.next
        l1 = l
        if l < k or k == 1:
            return head
        np = cp
        for i in range(k-1):
            np = np.next
        head = np
        np = cp.next
        tail1 = cp
        while l >= 0:
            tail = tail1
            tail1 = cp
            if l < k:
                tail.next = cp
                break
            for i in range(k-1):
                tmp = np
                np = np.next
                tmp.next = cp
                cp = tmp
            if l < l1:
                head1 = cp
                tail.next = head1
            l -= k
            cp = np
            if cp and cp.next:
                np = cp.next
        return head