# ─────────────────────────────────────────
# ADJACENCY LIST VERSION
# ─────────────────────────────────────────

def get_next_neighbor_list(neighbors, after=None):
    found = after is None
    for neighbor in neighbors:
        if not found:
            if neighbor == after:
                found = True
            continue
        return neighbor
    return None


def compute_indegree_list(graph):
    indegree = {node: 0 for node in range(len(graph))}
    node = 0

    while node < len(graph):
        neighbor = get_next_neighbor_list(graph[node])

        while neighbor is not None:
            indegree[neighbor] = indegree[neighbor] + 1
            neighbor = get_next_neighbor_list(graph[node], neighbor)

        node = node + 1

    return indegree


def kahns_list(graph):
    indegree = compute_indegree_list(graph)
    queue    = []
    order    = []

    # Seed queue with all nodes that have no incoming edges
    node = 0
    while node < len(graph):
        if indegree[node] == 0:
            queue.append(node)
        node = node + 1

    while queue:
        current_node = queue.pop(0)
        order.append(current_node)

        neighbor = get_next_neighbor_list(graph[current_node])

        while neighbor is not None:
            indegree[neighbor] = indegree[neighbor] - 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

            neighbor = get_next_neighbor_list(graph[current_node], neighbor)

    # If order doesn't contain all nodes, a cycle exists
    if len(order) != len(graph):
        return None     # cycle detected

    return order


# ─────────────────────────────────────────
# ADJACENCY MATRIX VERSION
# ─────────────────────────────────────────

def get_next_neighbor_matrix(row, after=None):
    start = 0 if after is None else after + 1

    for neighbor in range(start, len(row)):
        if row[neighbor] != 0:
            return neighbor

    return None


def compute_indegree_matrix(graph):
    indegree = {node: 0 for node in range(len(graph))}
    node = 0

    while node < len(graph):
        neighbor = get_next_neighbor_matrix(graph[node])

        while neighbor is not None:
            indegree[neighbor] = indegree[neighbor] + 1
            neighbor = get_next_neighbor_matrix(graph[node], neighbor)

        node = node + 1

    return indegree


def kahns_matrix(graph):
    indegree = compute_indegree_matrix(graph)
    queue    = []
    order    = []

    # Seed queue with all nodes that have no incoming edges
    node = 0
    while node < len(graph):
        if indegree[node] == 0:
            queue.append(node)
        node = node + 1

    while queue:
        current_node = queue.pop(0)
        order.append(current_node)

        neighbor = get_next_neighbor_matrix(graph[current_node])

        while neighbor is not None:
            indegree[neighbor] = indegree[neighbor] - 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

            neighbor = get_next_neighbor_matrix(graph[current_node], neighbor)

    # If order doesn't contain all nodes, a cycle exists
    if len(order) != len(graph):
        return None     # cycle detected

    return order


# ─────────────────────────────────────────
# PRINT HELPER
# ─────────────────────────────────────────

def print_order(order):
    index = 0
    while index < len(order):
        if index < len(order) - 1:
            print(order[index], end=" --> ")
        else:
            print(order[index])
        index = index + 1


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == '__main__':

    # Directed Acyclic Graph (DAG):
    #
    #   5 ──► 0 ◄── 4
    #   |           |
    #   ▼           ▼
    #   2 ──► 3 ──► 1
    #
    # Valid topological orders:
    # 4 → 5 → 0 → 2 → 3 → 1
    # 5 → 4 → 2 → 0 → 3 → 1  etc.

    adjacency_list = [
        [],         # Node 0 — no outgoing edges
        [],         # Node 1 — no outgoing edges
        [3],        # Node 2 → Node 3
        [1],        # Node 3 → Node 1
        [0, 1],     # Node 4 → Node 0, Node 1
        [0, 2]      # Node 5 → Node 0, Node 2
    ]

    adjacency_matrix = [
        [0, 0, 0, 0, 0, 0],   # Node 0
        [0, 0, 0, 0, 0, 0],   # Node 1
        [0, 0, 0, 1, 0, 0],   # Node 2
        [0, 1, 0, 0, 0, 0],   # Node 3
        [1, 1, 0, 0, 0, 0],   # Node 4
        [1, 0, 1, 0, 0, 0]    # Node 5
    ]

    # --- Adjacency List ---
    order = kahns_list(adjacency_list)
    print("=== Kahn's — Adjacency List ===")
    if order is None:
        print("Cycle detected — topological sort not possible!")
    else:
        print_order(order)

    print()

    # --- Adjacency Matrix ---
    order = kahns_matrix(adjacency_matrix)
    print("=== Kahn's — Adjacency Matrix ===")
    if order is None:
        print("Cycle detected — topological sort not possible!")
    else:
        print_order(order)

    print()

    # --- Cycle detection demo ---
    print("=== Cycle Detection Demo ===")
    cyclic_graph = [
        [1],    # Node 0 → Node 1
        [2],    # Node 1 → Node 2
        [0]     # Node 2 → Node 0  <-- cycle!
    ]
    order = kahns_list(cyclic_graph)
    if order is None:
        print("Cycle detected — topological sort not possible!")
    else:
        print_order(order)