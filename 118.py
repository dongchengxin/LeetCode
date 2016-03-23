class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pt = []
        if numRows > 0:
            pt.append([1])
        i = 1
        while i < numRows:
            pt.append([1])
            for j in range(i - 1):
                pt[i].append(pt[i-1][j] + pt[i-1][j+1])
            pt[i].append(1)
            i += 1
        return pt