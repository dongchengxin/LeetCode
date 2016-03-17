class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = []
        while n != 1:
            if n not in s:
                s.append(n)
                l = list(str(n))
                n = 0
                for c in l:
                    n += int(c) ** 2
            else:
                return False
        return True