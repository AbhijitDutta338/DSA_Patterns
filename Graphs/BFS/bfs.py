# ─────────────────────────────────────────
# ADJACENCY LIST VERSION
# ─────────────────────────────────────────

def get_next_neighbor_list(neighbors, visited, after=None):
    found = after is None
    for neighbor in neighbors:
        if not found:
            if neighbor == after:
                found = True
            continue
        if neighbor not in visited:
            return neighbor
    return None


def bfs_list(graph, source):
    visited = set()
    queue   = [source]
    order   = []

    visited.add(source)

    while queue:
        current_node = queue.pop(0)         # FIFO — pop from front
        order.append(current_node)

        neighbor = get_next_neighbor_list(graph[current_node], visited)

        while neighbor is not None:
            visited.add(neighbor)
            queue.append(neighbor)
            neighbor = get_next_neighbor_list(graph[current_node], visited, neighbor)

    return order


# ─────────────────────────────────────────
# ADJACENCY MATRIX VERSION
# ─────────────────────────────────────────

def get_next_neighbor_matrix(row, visited, after=None):
    start = 0 if after is None else after + 1

    for neighbor in range(start, len(row)):
        if row[neighbor] != 0 and neighbor not in visited:
            return neighbor

    return None


def bfs_matrix(graph, source):
    visited = set()
    queue   = [source]
    order   = []

    visited.add(source)

    while queue:
        current_node = queue.pop(0)         # FIFO — pop from front
        order.append(current_node)

        neighbor = get_next_neighbor_matrix(graph[current_node], visited)

        while neighbor is not None:
            visited.add(neighbor)
            queue.append(neighbor)
            neighbor = get_next_neighbor_matrix(graph[current_node], visited, neighbor)

    return order


# ─────────────────────────────────────────
# PRINT HELPER
# ─────────────────────────────────────────

def print_order(label, order):
    print(label, end=" : ")
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

    #        0
    #       / \
    #      1   2
    #     / \   \
    #    3   4   5
    #         \
    #          6

    adjacency_list = [
        [1, 2],     # Node 0
        [3, 4],     # Node 1
        [5],        # Node 2
        [],         # Node 3
        [6],        # Node 4
        [],         # Node 5
        []          # Node 6
    ]

    adjacency_matrix = [
        [0, 1, 1, 0, 0, 0, 0],   # Node 0
        [0, 0, 0, 1, 1, 0, 0],   # Node 1
        [0, 0, 0, 0, 0, 1, 0],   # Node 2
        [0, 0, 0, 0, 0, 0, 0],   # Node 3
        [0, 0, 0, 0, 0, 0, 1],   # Node 4
        [0, 0, 0, 0, 0, 0, 0],   # Node 5
        [0, 0, 0, 0, 0, 0, 0]    # Node 6
    ]

    source = 0

    print("=== BFS — Adjacency List ===")
    print_order("BFS", bfs_list(adjacency_list, source))

    print()

    print("=== BFS — Adjacency Matrix ===")
    print_order("BFS", bfs_matrix(adjacency_matrix, source))