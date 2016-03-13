class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        result = []
        l = len(nums)
        for j in range(l):
            if j + 1 < l and nums[j+1] - nums[j] == 1:
                j += 1
            elif j == i:
                result.append(str(nums[i]))
                i += 1
            else:
                result.append(str(nums[i])+"->"+str(nums[j]))
                i = j + 1
        return result