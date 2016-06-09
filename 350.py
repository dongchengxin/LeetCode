class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        result = []
        for i in nums1:
            d[i] = d.setdefault(i, 0) + 1
        for i in nums2:
            if i in d and d[i] > 0:
                d[i] -= 1
                result.append(i)
        return result
