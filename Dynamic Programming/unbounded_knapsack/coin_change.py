'''
You are given coins of different denominations and a total amount.
Each coin can be used unlimited times.
Goal: Minimize the number of coins to make up the amount. Return -1 if impossible.
'''
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[w] = min coins needed to make amount w
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # base case: 0 coins to make amount 0

        for i in range(len(coins)):
            coin = coins[i]

            for w in range(coin, amount + 1):  # start from coin value (can't use coin if w < coin)
                # Option 1: skip this coin → dp[w] (already stored)
                # Option 2: take this coin → dp[w - coin] + 1
                # Note: dp[w - coin] is from the CURRENT row (unbounded — reuse allowed)
                withCoin = dp[w - coin] + 1
                if withCoin < dp[w]:
                    dp[w] = withCoin

        return dp[amount] if dp[amount] != float('inf') else -1