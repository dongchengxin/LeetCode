class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = sum(26 ** i * (string.uppercase.index(c)+1) for (c,i) in zip(s[::-1],range(len(s))))
        return result