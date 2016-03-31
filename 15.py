class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lengthS = len(nums)
        if lengthS < 3:
            return []
        nums.sort()
        i = 0
        res = []
        while i < lengthS and nums[i] <= 0:
            l = i + 1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            r = lengthS - 1
            while r > l:
                if r < lengthS - 1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                if nums[i] + nums[l] + nums[r] == 0:
                    tmp = [nums[i],nums[l],nums[r]]
                    res.append(tmp)
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
        return res