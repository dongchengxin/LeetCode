class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        h = len(haystack)
        n = len(needle)
        if h < n:
            return -1
        def partial_table(string):
            table = [0]
            i = 0
            for s in string[1:]:
                while i > 0 and s != string[i]:
                    i = table[i - 1]
                if s == string[i]:
                    i += 1
                table.append(i)
            print table
            return table
        table = partial_table(needle)
        i = 0
        k = 0
        while i < h-n+1+k:
            while haystack[i] == needle[k]:
                i += 1
                k += 1
                if k == n:
                    return i - n
            if k > 0:
                k = table[k-1]
            else:
                i += 1
        return -1