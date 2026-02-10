# Top K Frequent Elements using Min Heap
    def top_k_frequent_elements_min_heap_approach(self, nums, k):
        count = Counter(nums)
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [heapq.heappop(min_heap)[1] for _ in range(k)][::-1]
