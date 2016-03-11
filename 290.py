class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strlst = str.split(' ')
        i = 0
        if len(pattern) != len(strlst):
            return False
        while i < len(pattern):
            j = i
            while j < len(pattern):
                if pattern[j] == pattern[i] and strlst[j] != strlst[i] or pattern[j] != pattern[i] and strlst[j] == strlst[i]:
                    return False
                j += 1
            i += 1
        else:
            return True