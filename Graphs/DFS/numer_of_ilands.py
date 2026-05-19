class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c, rows, cols)
                    count += 1

        return count

    def dfs(self, grid, r, c, rows, cols):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if grid[r][c] == '0':
            return

        grid[r][c] = '0'   # mark as visited

        self.dfs(grid, r + 1, c, rows, cols)
        self.dfs(grid, r - 1, c, rows, cols)
        self.dfs(grid, r, c + 1, rows, cols)
        self.dfs(grid, r, c - 1, rows, cols)