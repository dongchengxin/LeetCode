class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        i = len(s) - 1
        ronum = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        rom = 'IVXLCDM'
        res += ronum[s[i]]
        while i > 0:
            if rom.index(s[i-1]) < rom.index(s[i]):
                res -= ronum[s[i-1]]
                if i - 2 >= 0:
                    res += ronum[s[i-2]]
                i -= 2
            else:
                res += ronum[s[i-1]]
                i -= 1
        return res