class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, x in enumerate(nums):
            if target - x in index:
                return [index[target - x], i]
            index[x] = i

s = Solution()
nums = [1,4,9,17,25,39,56]
target = 56
print s.twoSum(nums,target)