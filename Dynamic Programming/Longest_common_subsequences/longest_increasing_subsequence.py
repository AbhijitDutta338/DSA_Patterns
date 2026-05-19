#Given an integer array nums, return the length of the longest strictly increasing subsequence.
'''Subsequence → elements keep order,Not required to be contiguous'''

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        # dp[i] = length of longest increasing subsequence ending at i
        dp = [1] * n  # each element itself is a subsequence of length 1
        maxLength = 1  # overall maximum length found

        # For each element, look at all previous elements to extend LIS
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # if nums[i] can extend subsequence ending at j
                    value = dp[j] + 1
                    if value > dp[i]:
                        dp[i] = value

            # update global maximum after processing position i
            if dp[i] > maxLength:
                maxLength = dp[i]

        return maxLength