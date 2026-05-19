import heapq

# ─────────────────────────────────────────
# ADJACENCY LIST VERSION
# ─────────────────────────────────────────

def get_next_neighbor_list(neighbors, visited, after=None):
    found = after is None
    for neighbor, weight in neighbors:
        if not found:
            if neighbor == after:
                found = True
            continue
        if neighbor not in visited:
            return neighbor, weight
    return None, None


def dijkstra_list(graph, source):
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

        neighbor, weight = get_next_neighbor_list(graph[current_node], visited)

        while neighbor is not None:
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_dist, neighbor))

            neighbor, weight = get_next_neighbor_list(graph[current_node], visited, neighbor)

    return distances, previous


# ─────────────────────────────────────────
# ADJACENCY MATRIX VERSION
# ─────────────────────────────────────────

def get_next_neighbor_matrix(row, visited, after=None):
    start = 0 if after is None else after + 1

    for neighbor in range(start, len(row)):
        weight = row[neighbor]
        if weight != 0 and neighbor not in visited:
            return neighbor, weight

    return None, None


def dijkstra_matrix(graph, source):
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

        neighbor, weight = get_next_neighbor_matrix(graph[current_node], visited)

        while neighbor is not None:
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_dist, neighbor))

            neighbor, weight = get_next_neighbor_matrix(graph[current_node], visited, neighbor)

    return distances, previous


# ─────────────────────────────────────────
# PATH RECONSTRUCTION (works for both)
# ─────────────────────────────────────────

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


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == '__main__':

    # Same graph, two representations
    #
    #   0 --(4)--> 1
    #   0 --(1)--> 2
    #   2 --(2)--> 1
    #   1 --(1)--> 3
    #   2 --(5)--> 3

    adjacency_list = [
        [(1, 4), (2, 1)],   # Node 0
        [(3, 1)],            # Node 1
        [(1, 2), (3, 5)],   # Node 2
        []                   # Node 3
    ]

    adjacency_matrix = [
        [0, 4, 1, 0],   # Node 0
        [0, 0, 0, 1],   # Node 1
        [0, 2, 0, 5],   # Node 2
        [0, 0, 0, 0]    # Node 3
    ]

    source      = 0
    destination = 3

    # --- Adjacency List ---
    distances_list, previous_list = dijkstra_list(adjacency_list, source)
    path_list = get_shortest_path(previous_list, source, destination)

    print("=== Adjacency List ===")
    print("Distances :", distances_list)
    print("Shortest path to node", destination, ":", path_list)
    print("Shortest distance to node", destination, ":", distances_list[destination])

    print()

    # --- Adjacency Matrix ---
    distances_matrix, previous_matrix = dijkstra_matrix(adjacency_matrix, source)
    path_matrix = get_shortest_path(previous_matrix, source, destination)

    print("=== Adjacency Matrix ===")
    print("Distances :", distances_matrix)
    print("Shortest path to node", destination, ":", path_matrix)
    print("Shortest distance to node", destination, ":", distances_matrix[destination])