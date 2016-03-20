# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = lenB = 0
        pa = headA
        pb = headB
        while pa:
            lenA += 1
            pa = pa.next
        while pb:
            lenB += 1
            pb = pb.next
        pa = headA
        pb = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                pa = pa.next
        else:
            for i in range(lenB - lenA):
                pb = pb.next
        while pa != pb:
            pa = pa.next
            pb = pb.next
        return pa