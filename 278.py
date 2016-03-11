# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i != j:
            if isBadVersion(i + (j-i)/2):
                j = i + (j-i)/2
            else:
                i = i + (j-i+1)/2
        return i