class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        s = zip(*strs)
        l = 0
        for col in s:
            if len(set(col)) == 1:
                l += 1
            else:
                break
        return strs[0][:l]