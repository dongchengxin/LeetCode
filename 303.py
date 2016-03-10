class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [0] * len(nums)
        for i,num in enumerate(nums):
            if i == 0:
            	self.sums[i] = nums[0]
            else:
            	self.sums[i] = self.sums[i - 1] + num

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i - 1]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
nums = [-2,0,3,-5,2,-1]
numArray = NumArray(nums)
print numArray.sumRange(0,2)
print numArray.sumRange(2,5)
print numArray.sumRange(0,5)