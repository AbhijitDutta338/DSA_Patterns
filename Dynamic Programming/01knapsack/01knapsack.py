'''
You are given: n items
weights[i] and values[i] for each item & a knapsack with capacity W, Each item can be taken at most once.
Goal:
Maximize total value without exceeding capacity.
'''
class Solution:
    def knapsack(self, weights: list[int], values: list[int], capacity: int) -> int:
        n = len(weights)
        # dp[i][w] = max value using first i items with capacity w
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        # Build table item by item
        for i in range(1, n + 1):
            itemWeight = weights[i - 1]
            itemValue = values[i - 1]

            for w in range(capacity + 1):
                # By default, do not take the current item
                dp[i][w] = dp[i - 1][w]

                # If capacity allows, consider taking the item and compare
                if w >= itemWeight:
                    valueWithItem = dp[i - 1][w - itemWeight] + itemValue
                    if valueWithItem > dp[i][w]:
                        dp[i][w] = valueWithItem

        # dp[n][capacity] is the maximum achievable value
        return dp[n][capacity]
