class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        h = 1
        n = num
        res = ''
        d = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        while n/10 > 0:
            h *= 10
            n /= 10
        n = num
        while n > 0:
            if n/h == 4:
                res = res + d[h] + d[5*h]
            elif n/h == 9:
                res = res + d[h] + d[10*h]
            elif n/h > 4:
                res = res + d[5*h] + (n/h-5)*d[h]
            else:
                res = res + n/h * d[h]
            n -= n / h * h
            h /= 10
        return res