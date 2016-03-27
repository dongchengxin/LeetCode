class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        r = len(height) - 1
        l = 0
        while l < r:
            if height[l] < height[r]:
                maxarea = max(maxarea, (r-l)*height[l])
                l += 1
            else:
                maxarea = max(maxarea, (r-l)*height[r])
                r -= 1
        return maxarea