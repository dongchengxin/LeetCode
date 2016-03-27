class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sign = 1
        if x > 2**31-1 or x < -(2**31-1):
            return res
        if x < 0:
            sign = -1
            x = abs(x)
        while x > 0:
            res = res * 10 + x % 10
            x = x / 10
        res *= sign
        if res > 2**31-1 or res < -(2**31-1):
            return 0
        return res