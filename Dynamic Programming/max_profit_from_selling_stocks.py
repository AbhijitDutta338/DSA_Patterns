#DP -> 0/1 Knapsack variant

class Solution:
    def maximumProfit(self, present: list[int], future: list[int], budget: int) -> int:
        n = len(present)
        dp = [0] * (budget + 1)

        for i in range(n):
            cost = present[i]
            profit = future[i] - present[i]

            if profit <= 0:
                continue

            for w in range(budget, cost - 1, -1):
                value = dp[w - cost] + profit
                if value > dp[w]:
                    dp[w] = value

        return dp[budget]
