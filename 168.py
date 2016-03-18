class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        m = 1
        n = n - 1
        while n >= 0:
            m = n % 26
            n = n / 26 - 1
            s = string.uppercase[m] + s
        return s