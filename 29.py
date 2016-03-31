class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend >= 0) ^ (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b:
            n, nb = 1, b
            while a >= nb:
                a, res = a - nb, res + n
                n, nb = n << 1, nb << 1
        return min(res,2147483647) if sign else max(-res,-2147483648)