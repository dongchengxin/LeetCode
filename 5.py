class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s
        i = l = r = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[start]:
                i += 1
            end = i - 1
            while start - 1 >= 0 and end + 1 < n and s[start-1] == s[end+1]:
                start -= 1
                end += 1
            if end - start >= r - l:
                l = start
                r = end
        return s[l:r+1]