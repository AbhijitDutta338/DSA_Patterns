#Fixed size continguous subarray of size k with maximum average
#Fixed Sliding Window
def find_max_average_sliding_window(self, nums, k):
    sum_window = sum(nums[:k])
    max_sum = sum_window

    for i in range(k, len(nums)):
        sum_window += nums[i] - nums[i - k]
        max_sum = max(max_sum, sum_window)
    
    return max_sum / k