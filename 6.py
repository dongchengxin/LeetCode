class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        l = len(s)
        res = ''
        for i in range(numRows):
            j = i
            k = 1
            if i == numRows - 1:
                k = 2
            while j < l:
                res = res + s[j]
                j = (k * (numRows-1) - j) + k * (numRows - 1)
                if i == 0 or i == numRows - 1:
                    k += 2
                else:
                    k += 1
        return res