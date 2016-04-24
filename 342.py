class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        binum = bin(num)[2:]
        l = len(binum)
        if l % 2 == 0:
            return False
        for i in range(1, l):
            if binum[i] == '1':
                return False
        return True
