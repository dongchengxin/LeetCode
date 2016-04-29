class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        r = length - 1
        l = 0
        n1 = r
        while l <= n1:
            mid1 = (l + n1) / 2
            if nums[mid1] < target:
                l = mid1 + 1
            else:
                n1 = mid1 - 1
        n2 = l
        while n2 <= r:
            mid2 = (n2 + r) / 2
            if nums[mid2] > target:
                r = mid2 - 1
            else:
                n2 = mid2 + 1
        return [l, r] if l <= r else [-1, -1]
