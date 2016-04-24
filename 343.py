class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        return self.func(n)

    def func(self, n):
        if n >= 7:
            return 3 * self.func(n - 3)
        elif n == 4:
            return 4
        else:
            return 3 * (n - 3)
