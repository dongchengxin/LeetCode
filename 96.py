class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fac(2 * n) / (self.fac(n) * self.fac(n + 1))

    def fac(self, n):
        if n < 2:
            return 1
        return n * self.fac(n - 1)
