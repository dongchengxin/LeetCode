class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(bin(n).replace('0b',''))
        s.reverse()
        s.extend(['0']*(32 - len(s)))
        return int(''.join(s),2)