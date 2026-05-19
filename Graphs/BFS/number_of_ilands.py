from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.bfs(grid, r, c, rows, cols)
                    count += 1

        return count

    def bfs(self, grid, r, c, rows, cols):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))
