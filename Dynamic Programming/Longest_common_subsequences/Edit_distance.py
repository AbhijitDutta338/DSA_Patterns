'''
Given two strings word1 and word2, return the minimum number of operations
to convert word1 into word2.
Allowed operations (each costs 1):
- Insert a character
- Delete a character
- Replace a character
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # lengths of the input strings
        m = len(word1)
        n = len(word2)

        # dp[i][j] = min operations to convert word1[:i] to word2[:j]
        # use (m+1) x (n+1) table with extra row/column for empty string base cases
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: converting any prefix to empty string = delete all chars
        for i in range(m + 1):
            dp[i][0] = i
        # Base case: converting empty string to any prefix = insert all chars
        for j in range(n + 1):
            dp[0][j] = j

        # Fill the DP table row by row for increasing prefixes
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If current characters match, no operation needed — carry forward
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Replace: both pointers move → dp[i-1][j-1]
                    # Delete:  move word1 pointer → dp[i-1][j]
                    # Insert:  move word2 pointer → dp[i][j-1]
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                       dp[i - 1][j],
                                       dp[i][j - 1])

        # dp[m][n] holds the min edit distance for full strings
        return dp[m][n]