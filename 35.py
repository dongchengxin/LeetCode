class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if target <= nums[l]:
            return 0
        elif target > nums[r]:
            return r + 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        return r
