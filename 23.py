# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)
        head = ListNode(0)
        p = head
        tmp = []
        for i in range(l):
            while lists[i]:
                tmp.append(lists[i].val)
                lists[i] = lists[i].next
        tmp.sort()
        l = len(tmp)
        for i in range(l):
            p.next = ListNode(tmp[i])
            p = p.next
        return head.next