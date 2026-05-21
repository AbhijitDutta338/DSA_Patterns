# ─────────────────────────────────────────
# LONGEST PALINDROMIC SUBSTRING
# ─────────────────────────────────────────
# Goal — find the longest substring of a string that reads
#         the same forwards and backwards
#
# Approach — Expand Around Center
#   LCS (string, reversed_string) gives longest palindromic subsequence, but not substring

class Solution:
    def longestPalindromeSubsequence(self, s: str) -> str:
        # This function should return the longest palindromic subsequence
        return self.longestCommonSubsequence(s, s[::-1])

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # lengths of the input strings
        m = len(text1)
        n = len(text2)

        # dp[i][j] = length of LCS of text1[:i] and text2[:j]
        # use (m+1) x (n+1) table with extra zero row/column for empty prefixes
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table row by row for increasing prefixes
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If current characters match, extend the previous common subsequence
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Otherwise take the best of skipping one char from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # dp[m][n] holds the LCS length for full strings
        return dp[m][n]