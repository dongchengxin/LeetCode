class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        i = 0
        pt = [[],[]]
        pt[0] = [1]
        while i < rowIndex:
            pt[(i+1)%2] = [1]
            for j in range(i):
                pt[(i+1)%2].append(pt[i%2][j]+pt[i%2][j+1])
            pt[(i+1)%2].append(1)
            i += 1
        return pt[rowIndex%2]