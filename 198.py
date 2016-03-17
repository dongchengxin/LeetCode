class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        else:
            sums = [0] * l
            sums[0] = nums[0]
            sums[1] = max(nums[0],nums[1])
        for i in range(2,l):
            sums[i] = max(sums[i-1],nums[i]+sums[i-2])
        return sums[l-1]