class Solution(object):
    def nQueens(self, n):
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def is_safe(row, col):
            # Check the column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check the upper left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check the upper right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        backtrack(0)
        return result