class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= target < nums[mid]:
                r = mid
            elif nums[mid] < target <= nums[r]:
                l = mid
            elif nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        return -1
