class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        h = 1
        r = x
        while (r/10)>0:
            h *= 10
            r /= 10
        r = x
        while r > 0:
            if r/h != r%10:
                return False
            r = (r - r/h*h) / 10
            h /= 100
        return True