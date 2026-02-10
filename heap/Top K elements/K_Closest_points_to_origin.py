# K Closest Points to Origin using Max Heap
    def get_distance(self, point):
        return point[0] ** 2 + point[1] ** 2

    def k_closest_points_to_origin_max_heap_approach(self, points, k):
        max_heap = []
        for point in points:
            heapq.heappush(max_heap, (-self.get_distance(point), point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)][::-1]