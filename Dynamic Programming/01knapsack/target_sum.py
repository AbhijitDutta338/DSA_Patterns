'''
Given an array of integers and a target, assign + or - to each number.
Goal: Count the number of ways to reach the target sum.

Key insight:
    Let P = subset assigned +, N = subset assigned -
    P + N = total
    P - N = target
    Solving → P = (total + target) / 2
    So: count subsets that sum to (total + target) / 2
'''
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)

        # target out of range or sum+target is odd → impossible
        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        subsetSum = (total + target) // 2
        n = len(nums)

        # dp[i][w] = number of ways to reach sum w using first i items
        dp = [[0] * (subsetSum + 1) for _ in range(n + 1)]

        # Base case: one way to reach sum 0 (pick nothing)
        dp[0][0] = 1

        for i in range(1, n + 1):
            num = nums[i - 1]

            for w in range(subsetSum + 1):
                # Option 1: skip current number
                dp[i][w] = dp[i - 1][w]

                # Option 2: take current number (if it fits)
                if w >= num:
                    dp[i][w] += dp[i - 1][w - num]

        return dp[n][subsetSum]