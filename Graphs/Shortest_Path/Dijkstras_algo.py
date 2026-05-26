import heapq

dist = [float('inf')] * numNodes  #Shortest path from source to each node initialization
dist[source] = 0

#priority Queue or min heap to find the least distance node.
min_heap = [(0, source)]  # (distance, node) 

while min_heap:
    d, node = heapq.heappop(min_heap)

    if d > dist[node]:
        continue  # found a better path already

    for (neighbor, weight) in node.edges:
        newDist = d + weight

        if newDist < dist[neighbor]:
            dist[neighbor] = newDist
            #min heap contains the least distance.
            heapq.heappush(min_heap, (newDist, neighbor))