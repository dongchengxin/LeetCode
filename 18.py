class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        len_num = len(nums)
        if len_num < 4:
            return []
        nums.sort()
        res = []
        i = 0
        for i in xrange(len_num-3):
            if i > 0 and nums[i] == nums[i-1] or nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            for j in xrange(len_num-1,i+2,-1):
                if j < len_num - 1 and nums[j] == nums[j+1] or nums[i] + nums[i+1] + nums[i+2] + nums[j] > target:
                    continue
                if nums[i] + nums[j] + nums[j-1] + nums[j-2] < target:
                    break
                l = i + 1
                r = j - 1
                while r > l:
                    if l > i + 1 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    if nums[i] + nums[l] + nums[l+1] + nums[j] > target or nums[i] + nums[r-1] + nums[r] + nums[j] < target:
                        break
                    x = nums[i] + nums[j] + nums[l] + nums[r]
                    if x == target:
                        res.append([nums[i],nums[l],nums[r],nums[j]])
                        l += 1
                        r -= 1
                    elif x > target:
                        r -= 1
                    else:
                        l += 1
        return res