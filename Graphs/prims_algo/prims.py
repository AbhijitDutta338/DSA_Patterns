import heapq
import math

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


def prims_list(graph, source):
    visited   = set()
    mst_edges = []
    total_cost = 0

    # (weight, from_node, to_node)
    priority_queue = [(0, source, source)]

    while priority_queue:
        weight, from_node, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node != source:
            mst_edges.append((from_node, current_node, weight))
            total_cost = total_cost + weight

        neighbor, edge_weight = get_next_neighbor_list(graph[current_node], visited)

        while neighbor is not None:
            heapq.heappush(priority_queue, (edge_weight, current_node, neighbor))
            neighbor, edge_weight = get_next_neighbor_list(graph[current_node], visited, neighbor)

    return mst_edges, total_cost


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


def prims_matrix(graph, source):
    visited    = set()
    mst_edges  = []
    total_cost = 0

    # (weight, from_node, to_node)
    priority_queue = [(0, source, source)]

    while priority_queue:
        weight, from_node, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node != source:
            mst_edges.append((from_node, current_node, weight))
            total_cost = total_cost + weight

        neighbor, edge_weight = get_next_neighbor_matrix(graph[current_node], visited)

        while neighbor is not None:
            heapq.heappush(priority_queue, (edge_weight, current_node, neighbor))
            neighbor, edge_weight = get_next_neighbor_matrix(graph[current_node], visited, neighbor)

    return mst_edges, total_cost


# ─────────────────────────────────────────
# PRINT MST HELPER
# ─────────────────────────────────────────

def print_mst(mst_edges, total_cost):
    edge_index = 0
    while edge_index < len(mst_edges):
        from_node, to_node, weight = mst_edges[edge_index]
        print("  Node", from_node, "--(" , weight , ")--> Node", to_node)
        edge_index = edge_index + 1
    print("  Total MST cost:", total_cost)


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == '__main__':

    # Graph (undirected — edges go both ways):
    #
    #       2       3
    #   0 ───── 1 ───── 3
    #   |       |       |
    # 6 |     8 |       | 9
    #   |       |       |
    #   2 ───── 4 ───── 5
    #       5       7

    adjacency_list = [
        [(1, 2), (2, 6)],              # Node 0
        [(0, 2), (3, 3), (4, 8)],      # Node 1
        [(0, 6), (4, 5)],              # Node 2
        [(1, 3), (5, 9)],              # Node 3
        [(1, 8), (2, 5), (5, 7)],      # Node 4
        [(3, 9), (4, 7)]               # Node 5
    ]

    adjacency_matrix = [
        [0, 2, 6, 0, 0, 0],   # Node 0
        [2, 0, 0, 3, 8, 0],   # Node 1
        [6, 0, 0, 0, 5, 0],   # Node 2
        [0, 3, 0, 0, 0, 9],   # Node 3
        [0, 8, 5, 0, 0, 7],   # Node 4
        [0, 0, 0, 9, 7, 0]    # Node 5
    ]

    source = 0

    # --- Adjacency List ---
    mst_edges, total_cost = prims_list(adjacency_list, source)
    print("=== Prim's — Adjacency List ===")
    print_mst(mst_edges, total_cost)

    print()

    # --- Adjacency Matrix ---
    mst_edges, total_cost = prims_matrix(adjacency_matrix, source)
    print("=== Prim's — Adjacency Matrix ===")
    print_mst(mst_edges, total_cost)