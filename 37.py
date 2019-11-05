from collections import defaultdict

class Solution(object):

    solved = False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def could_place_number(d, row, col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
        
        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'
        
        def box_index(row, col):
            return (row / 3) * 3 + col / 3
        
        def place_next_number(row, col):
            if row == N-1 and col == N-1:
                Solution.solved = True
            else:
                if col == N - 1:
                    backtrace(row+1, 0)
                else:
                    backtrace(row, col+1)
        
        def backtrace(row=0, col=0):
            if board[row][col] == '.':
                for d in range(1, N+1):
                    if could_place_number(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)
                        if not Solution.solved:
                            remove_number(d, row, col)
            else:
                place_next_number(row, col)
        
        N = 9
        
        rows = [defaultdict(int) for i in range(N)]
        cols = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                d = board[i][j]
                if d != '.':
                    place_number(int(d), i, j)
        backtrace()

if __name__ == "__main__":
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    Solution().solveSudoku(board)
    print board
