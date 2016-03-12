class Solution(object):
	def isPowerOfTwo(self,n):
		"""
		:type n: int
		:rtype: bool
		"""
		if n <= 0:
			return False
		return 2**31 % n == 0