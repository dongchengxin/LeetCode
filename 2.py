# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = ListNode(0)
        l4 = l3
        while l1 or l2 or carry:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            x = a + b + carry
            l3.next = ListNode(x % 10)
            #carry = x / 10             除法效率较低
            if x >= 10:
                carry = 1
            else:
                carry = 0
            l3 = l3.next
        return l4.next