class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isRowValid(board) and self.isColValid(board) and self.isSqValid(board)

    def isRowValid(self, board):
        for row in board:
            if len(row) != 9 or len(set(row)) != len(row) - row.count('.') + 1:
                return False
        return True

    def isColValid(self, board):
        for col in zip(*board):
            if len(col) != 9 or len(set(col)) != len(col) - col.count('.') + 1:
                return False
        return True

    def isSqValid(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if len(set(square)) != len(square) - square.count('.') + 1:
                    return False
        return True