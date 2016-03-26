class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current = '1'
        while n > 1:
            next = ''.join([str(len(list(g))) + k for k, g in itertools.groupby(current)])
            current = next
            n -= 1
        return current