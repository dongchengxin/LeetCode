class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = []
        a = b = l = 0
        for i,c in enumerate(s):
            if c in ss:
                a = s.find(c,a)
                d = len(ss)
                if d > l:
                    l = d
                b = ss.index(c)
                ss[:b+1] = []
            ss.append(c)
        d = len(ss)
        if d > l:
            l = d
        return l