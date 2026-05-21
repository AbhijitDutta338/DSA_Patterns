'''
Given an array of integers, determine if it can be partitioned into
two subsets with equal sum.
Goal: Check if any subset sums to total/2.
'''
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        # Odd total can never be split equally
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        # dp[i][w] = can we reach sum w using first i items
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # Base case: sum of 0 is always reachable (pick nothing)
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            num = nums[i - 1]

            for w in range(target + 1):
                # Option 1: skip current number
                dp[i][w] = dp[i - 1][w]

                # Option 2: take current number (if it fits)
                if w >= num:
                    dp[i][w] = dp[i][w] or dp[i - 1][w - num]

        return dp[n][target]