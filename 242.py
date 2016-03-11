class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map = {}
        for i in range(len(s)):
            map[s[i]] = map.setdefault(s[i],0) + 1
            map[t[i]] = map.setdefault(t[i],0) - 1
        for i in map:
            if map.get(i) != 0:
                return False
        return True