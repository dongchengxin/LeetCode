class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = z = 0
        while i + z < n:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                z += 1
            else:
                i += 1