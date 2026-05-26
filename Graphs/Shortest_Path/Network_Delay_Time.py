'''
You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.
'''

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Build the graph
        graph = {u:[] for u in range(1, n+1)}

        for u, v, time in times:
            graph[u].append((v, time))

        #Dijstras Algo
        required_time  = [float('inf')] * (n+1)
        required_time[k] = 0

        heap = [(0, k)]

        while heap:
            t, node = heapq.heappop(heap)

            if t > required_time[node]:
                continue

            for (neighbor, time) in graph[node]:
                newTime = t + time

                if newTime < required_time[neighbor]:
                    required_time[neighbor] = newTime
                    heapq.heappush(heap, (newTime, neighbor))
        
        #get the minimum time
        minTime = max(required_time[1:])
        return minTime if minTime != float('inf') else -1

# TODO: Add the Neetcode Solution as well, its more optimized.