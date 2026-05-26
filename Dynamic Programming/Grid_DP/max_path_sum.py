'''
Maximum path sum in a matrix with restricted movement.
You start at:
Bottom-left: (m-1, 0) if using 0-based indexing
End at top-right: (0, n-1)

Allowed moves: Up → (i-1, j) | Right → (i, j+1)
Goal: Maximize total sum of visited cells.'''

class solution:
    def max_path(grid):

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        # Start point
        dp[m - 1][0] = grid[m - 1][0]

        # Bottom row
        for j in range(1, n):
            dp[m - 1][j] = dp[m - 1][j - 1] + grid[m - 1][j]

        # First column
        for i in range(m - 2, -1, -1):
            dp[i][0] = dp[i + 1][0] + grid[i][0]

        # Remaining cells
        for i in range(m - 2, -1, -1):
            for j in range(1, n):

                dp[i][j] = grid[i][j] + max(
                    dp[i + 1][j],   # from below
                    dp[i][j - 1]    # from left
                )

        return dp[0][n - 1]