class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_num = len(nums)
        nums.sort()
        firstThree = nums[0] + nums[1] + nums[2]
        if firstThree >= target:
            return firstThree
        lastThree = nums[-1] + nums[-2] + nums[-3]
        if lastThree <= target:
            return lastThree
        mindiff = 2**31
        i = 0
        res = 0
        while i < len_num - 2 and 3*nums[i] <= target:
            l = i + 1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            r = len_num - 1
            while r > l:
                if r < len_num - 1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                x = nums[i] + nums[l] + nums[r] - target
                abx = abs(x)
                if abx < mindiff:
                    res = x + target
                    mindiff = abx
                if x < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
        return res