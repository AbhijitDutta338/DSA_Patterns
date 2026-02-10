import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-x for x in stones]
        
        heapq.heapify(weights)
        
        while(len(weights)>1):
            a = -1*heapq.heappop(weights)
            b = -1*heapq.heappop(weights)
            if(a!=b):
                heapq.heappush(weights, -1*abs(a-b))
        if(weights):
            return -1*weights[0]
        return 0