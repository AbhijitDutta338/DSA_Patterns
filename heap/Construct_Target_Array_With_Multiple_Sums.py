import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest

            if largest == 1 or rest == 1:
                return True

            if rest == 0 or largest <= rest:
                return False

            prev = largest % rest
            if prev == 0:
                return False

            heapq.heappush(heap, -prev)
            total = rest + prev