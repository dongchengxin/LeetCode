class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[left]:
                nums[left+1] = nums[i]
                left += 1
        return left + 1