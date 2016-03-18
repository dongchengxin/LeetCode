class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = {}
        for num in nums:
            s[num] = s.setdefault(num,0) + 1
        for key in s:
            if s[key] > n / 2:
                return key