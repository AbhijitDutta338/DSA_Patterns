class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[e])
        path = set()

        #Backtrack - dfs
        def dfs(r, c, i):
            if i == len(word): #Base condition
                return True
            
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            #Add option
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c +1, i + 1) or
                dfs(r, c -1, i+1))
            
            #Remove Option
            path.remove((r, c))

            #return boolean value
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False