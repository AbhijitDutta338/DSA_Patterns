import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in range(len(graph))}
    distances[source] = 0
    previous = {node: None for node in range(len(graph))}
    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        neighbor, weight = get_next_neighbor(graph[current_node], visited)

        while neighbor is not None:
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_dist, neighbor))

            neighbor, weight = get_next_neighbor(graph[current_node], visited, neighbor)

    return distances, previous


def get_next_neighbor(neighbors, visited, after=None):
    found = after is None
    for neighbor, weight in neighbors:
        if not found:
            if neighbor == after:
                found = True
            continue
        if neighbor not in visited:
            return neighbor, weight
    return None, None

def get_shortest_path(previous, source, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == source:
        return path
    else:
        return []  # no path exists

if __name__ == '__main__':
    # Graph as adjacency list: graph[node] = [(neighbor, weight), ...]
    graph = [
        [(1, 4), (2, 1)],        # Node 0 -> Node 1 (weight 4), Node 2 (weight 1)
        [(3, 1)],                 # Node 1 -> Node 3 (weight 1)
        [(1, 2), (3, 5)],        # Node 2 -> Node 1 (weight 2), Node 3 (weight 5)
        []                        # Node 3 -> no outgoing edges
    ]

    source = 0
    shortest_path, previous = dijkstra(graph, source)

    print("Shortest distances from node", source)
    print(shortest_path)
    print("\nPrevious nodes (for path reconstruction):")
    print(previous)

    path = get_shortest_path(previous, source, destination=3)
    print("Shortest distance:", shortest_path[3])
    print("Shortest path:", path)