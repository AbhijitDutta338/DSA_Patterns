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


def dfs_list(graph, source):
    visited = set()
    stack   = [source]
    order   = []

    while stack:
        current_node = stack.pop()          # LIFO — pop from top
        
        if current_node in visited:
            continue
        visited.add(current_node)
        order.append(current_node)

        neighbor = get_next_neighbor_list(graph[current_node], visited)

        while neighbor is not None:
            stack.append(neighbor)
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


def dfs_matrix(graph, source):
    visited = set()
    stack   = [source]
    order   = []

    while stack:
        current_node = stack.pop()          # LIFO — pop from top

        if current_node in visited:
            continue
        visited.add(current_node)
        order.append(current_node)

        neighbor = get_next_neighbor_matrix(graph[current_node], visited)

        while neighbor is not None:
            stack.append(neighbor)
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

    print("=== DFS — Adjacency List ===")
    print_order("DFS", dfs_list(adjacency_list, source))

    print()

    print("=== DFS — Adjacency Matrix ===")
    print_order("DFS", dfs_matrix(adjacency_matrix, source))