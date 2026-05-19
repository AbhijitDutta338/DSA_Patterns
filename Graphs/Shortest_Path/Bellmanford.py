import math

# ─────────────────────────────────────────
# ADJACENCY LIST VERSION
# ─────────────────────────────────────────

def get_next_neighbor_list(neighbors, after=None):
    found = after is None
    for neighbor, weight in neighbors:
        if not found:
            if neighbor == after:
                found = True
            continue
        return neighbor, weight
    return None, None


def bellman_ford_list(graph, source):
    distances = {node: math.inf for node in range(len(graph))}
    distances[source] = 0
    previous = {node: None for node in range(len(graph))}

    iteration = 0

    while iteration < len(graph) - 1:
        node = 0

        while node < len(graph):
            neighbor, weight = get_next_neighbor_list(graph[node])

            while neighbor is not None:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    previous[neighbor] = node

                neighbor, weight = get_next_neighbor_list(graph[node], neighbor)

            node = node + 1

        iteration = iteration + 1

    # Negative cycle detection
    node = 0
    while node < len(graph):
        neighbor, weight = get_next_neighbor_list(graph[node])

        while neighbor is not None:
            if distances[node] + weight < distances[neighbor]:
                return None, None  # Negative cycle detected

            neighbor, weight = get_next_neighbor_list(graph[node], neighbor)

        node = node + 1

    return distances, previous


# ─────────────────────────────────────────
# ADJACENCY MATRIX VERSION
# ─────────────────────────────────────────

def get_next_neighbor_matrix(row, after=None):
    start = 0 if after is None else after + 1

    for neighbor in range(start, len(row)):
        weight = row[neighbor]
        if weight != 0:
            return neighbor, weight

    return None, None


def bellman_ford_matrix(graph, source):
    distances = {node: math.inf for node in range(len(graph))}
    distances[source] = 0
    previous = {node: None for node in range(len(graph))}

    iteration = 0

    while iteration < len(graph) - 1:
        node = 0

        while node < len(graph):
            neighbor, weight = get_next_neighbor_matrix(graph[node])

            while neighbor is not None:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    previous[neighbor] = node

                neighbor, weight = get_next_neighbor_matrix(graph[node], neighbor)

            node = node + 1

        iteration = iteration + 1

    # Negative cycle detection
    node = 0
    while node < len(graph):
        neighbor, weight = get_next_neighbor_matrix(graph[node])

        while neighbor is not None:
            if distances[node] + weight < distances[neighbor]:
                return None, None  # Negative cycle detected

            neighbor, weight = get_next_neighbor_matrix(graph[node], neighbor)

        node = node + 1

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
    # Bellman-Ford supports negative weights!
    #
    #   0 --(4)--> 1
    #   0 --(1)--> 2
    #   2 --(-2)--> 1    <-- negative weight
    #   1 --(1)--> 3
    #   2 --(5)--> 3

    adjacency_list = [
        [(1, 4), (2, 1)],    # Node 0
        [(3, 1)],             # Node 1
        [(1, -2), (3, 5)],   # Node 2  <-- negative weight
        []                    # Node 3
    ]

    adjacency_matrix = [
        [0,  4,  1,  0],   # Node 0
        [0,  0,  0,  1],   # Node 1
        [0, -2,  0,  5],   # Node 2  <-- negative weight
        [0,  0,  0,  0]    # Node 3
    ]

    source      = 0
    destination = 3

    # --- Adjacency List ---
    result = bellman_ford_list(adjacency_list, source)

    print("=== Adjacency List ===")
    if result[0] is None:
        print("Negative cycle detected!")
    else:
        distances, previous = result
        path = get_shortest_path(previous, source, destination)
        print("Distances :", distances)
        print("Shortest path to node", destination, ":", path)
        print("Shortest distance to node", destination, ":", distances[destination])

    print()

    # --- Adjacency Matrix ---
    result = bellman_ford_matrix(adjacency_matrix, source)

    print("=== Adjacency Matrix ===")
    if result[0] is None:
        print("Negative cycle detected!")
    else:
        distances, previous = result
        path = get_shortest_path(previous, source, destination)
        print("Distances :", distances)
        print("Shortest path to node", destination, ":", path)
        print("Shortest distance to node", destination, ":", distances[destination])