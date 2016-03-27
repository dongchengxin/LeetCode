class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        res = 0
        sign = 1
        for i,c in enumerate(str.strip()):
            if c not in string.digits:
                if i == 0:
                    if c == '+':
                        sign = 1
                    elif c == '-':
                        sign = -1
                    else:
                        break
                else:
                    break
                continue
            res = res * 10 + int(c)
        res = res * sign
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        return res