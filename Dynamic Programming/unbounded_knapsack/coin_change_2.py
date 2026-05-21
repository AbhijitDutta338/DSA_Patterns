'''
You are given coins of different denominations and a total amount.
Each coin can be used unlimited times.
Goal: Count the number of combinations that make up the amount.
'''
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # dp[w] = number of ways to make amount w
        dp = [0] * (amount + 1)
        dp[0] = 1  # base case: one way to make amount 0 (use nothing)

        for i in range(len(coins)):
            coin = coins[i]

            for w in range(coin, amount + 1):
                # Add ways to make (w - coin), since we can reuse this coin
                dp[w] += dp[w - coin]

        return dp[amount]