class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while n/(5*i) > 0:
            count += n/(5*i)
            i *= 5
        return count