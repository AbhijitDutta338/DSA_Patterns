class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[e])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            #Base Case
            if ((r, c) in visit or #node already visited 
                r < 0 or c < 0 or r == ROWS or c == COLS or #(r,c) out of bounds
                heights[r][c] <prevHeight): #water flow condition failure
                return
        
            visit.add((r, c))
        
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(e, c, pac, heights[e][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, e, pac, heights[r][e])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res =[]
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res. append([r, c])

        return res