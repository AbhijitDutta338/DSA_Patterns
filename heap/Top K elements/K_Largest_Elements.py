def k_largest_elements_max_heap_approach(self, nums, k):
    return heapq.nlargest(k, nums)