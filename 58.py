class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = s.split()
        l = len(lst)
        if l > 0:
            return len(lst[l-1])
        return 0