class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        m = (l1 + l2 + 1) / 2
        n = (l1 + l2 + 2) / 2
        return (getkth(nums1,0,nums2,0,m) + getkth(nums1,0,nums2,0,n)) / 2.0
    
def getkth(l1, s1, l2, s2, k):
    if s1 > len(l1) - 1:
        return l2[s2 + k - 1]
    if s2 > len(l2) - 1:
        return l1[s1 + k - 1]
    if k == 1:
        return min(l1[s1], l2[s2])
    l1_mid = float('Inf')
    l2_mid = float('Inf')
    if s1 + k/2 - 1 < len(l1):
        l1_mid = l1[s1 + k/2 - 1]
    if s2 + k/2 - 1 < len(l2):
        l2_mid = l2[s2 + k/2 - 1]
    if l1_mid < l2_mid:
        return getkth(l1, s1+k/2, l2, s2, k-k/2)
    else:
        return getkth(l1, s1, l2, s2+k/2, k-k/2)