class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        while l > 0:
            if digits[l-1] == 9:
                digits[l-1] = 0
                l -= 1
            else:
                digits[l-1] += 1
                break
        if l == 0:
            digits.insert(0,1)
        return digits