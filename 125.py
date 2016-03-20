class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ts = [c for c in s.lower() if c in string.digits+string.lowercase]
        return ts == ts[::-1]