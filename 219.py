class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        l = len(nums)
        if len(set(nums)) == len(nums):
            return False
        if k >= l:
            return len(set(nums)) < l
        while i + k < l:
            s = set(nums[i:i+k+1])
            if len(s) <= k:
                return True
            i += 1
        return False

        """
        hash method
        d = {}
        for i in range(len(nums)):
            t = nums[i]
            if not t in d or i - d[t] > k:
                d[t] = i
            else:
                return True
        return False
        """