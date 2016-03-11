# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        if l < 2:
            return True
        halfl = l / 2
        p = q = head
        i = 0
        for i in range(halfl):
            q = q.next
        cp = q
        np = cp.next
        cp.next = None
        for i in range(halfl):
            if np:
                tmp = np
                np = np.next
                tmp.next = cp
                cp = tmp
        q = cp
        while p and q:
            if p.val != q.val:
                b = False
                break
            p = p.next
            q = q.next
        else:
            b = True
        np = cp.next
        cp.next = None
        for i in range(halfl):
            if np:
                tmp = np
                np = np.next
                tmp.next = cp
                cp = tmp
        return b