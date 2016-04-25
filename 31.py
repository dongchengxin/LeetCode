class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pos = i
                break
        if pos == None:
            nums.reverse()
            return
        best = None
        for i in range(pos + 1, len(nums)):
            if best == None:
                best = i
            elif nums[pos] < nums[i] and nums[i] <= nums[best]:
                best = i
        nums[pos], nums[best] = nums[best], nums[pos]
        nums[pos + 1:] = nums[pos + 1:][::-1]
