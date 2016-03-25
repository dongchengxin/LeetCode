class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = 1
        for m in range(n):
            tmp = j
            j = i + j
            i = tmp
        return j