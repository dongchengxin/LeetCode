class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        for i,c in enumerate(s):
            d1.setdefault(c,[]).append(i)
        for i,c in enumerate(t):
            d2.setdefault(c,[]).append(i)
        l = len(d1)
        if l != len(d2):
            return False
        elif l <= 1:
            return True
        for key in d1:
            if d1[key] != d2[t[d1[key][0]]]:
                return False
        else:
            return True