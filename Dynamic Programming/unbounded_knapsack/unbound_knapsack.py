'''
You are given: n items
weights[i] and values[i] for each item & a knapsack with capacity W.
Each item can be taken ANY number of times.
Goal:
Maximize total value without exceeding capacity.
'''
class Solution:
    def unboundedKnapsack(self, weights: list[int], values: list[int], capacity: int) -> int:
        n = len(weights)
        # dp[w] = max value achievable with exactly capacity w
        dp = [0] * (capacity + 1)

        # Build table item by item
        for i in range(n):
            itemWeight = weights[i]
            itemValue = values[i]

            for w in range(itemWeight, capacity + 1):  # left→right so dp[w - itemWeight] is already updated
                # Option 1: skip this item → dp[w] (already stored)
                # Option 2: take this item → dp[w - itemWeight] + itemValue
                # Note: dp[w - itemWeight] is from CURRENT pass (unbounded — reuse allowed)
                valueWithItem = dp[w - itemWeight] + itemValue
                if valueWithItem > dp[w]:
                    dp[w] = valueWithItem

        return dp[capacity]