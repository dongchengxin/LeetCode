class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #use re module
        ma = re.match(p, s)
        if ma != None and ma.group() == s:
            return True
        return False