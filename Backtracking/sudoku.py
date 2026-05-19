class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_safe(row, col, num):
            # Check row
            if num in board[row]:
                return False

            # Check column
            for r in range(9):
                if board[r][col] == num:
                    return False

            # Check 3x3 box
            box_row = (row // 3) * 3
            box_col = (col // 3) * 3
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if board[r][c] == num:
                        return False
            
            return True
        
        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':

                        for num in '123456789':
                            if is_safe(row, col, num):
                                # Place the number (include)
                                board[row][col] = num

                                # Recurse — if solved, bubble True up
                                if backtrack():
                                    return True

                                # Undo the placement (exclude / go back)
                                board[row][col] = '.'
                        
                        # No number worked — trigger backtrack
                        return False

            # No empty cell found — board is solved
            return True

        backtrack()