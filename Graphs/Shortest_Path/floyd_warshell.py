import math

# ─────────────────────────────────────────
# FLOYD WARSHALL
# ─────────────────────────────────────────
# Works directly on an adjacency matrix
# No adjacency list version — Floyd-Warshall
# is inherently a matrix algorithm (dist[i][j])

def initialize_dist(graph, n):
    dist = []
    row  = 0

    while row < n:
        dist_row = []
        col      = 0

        while col < n:
            if row == col:
                dist_row.append(0)              # distance to self is 0

            elif graph[row][col] != 0:
                dist_row.append(graph[row][col]) # direct edge weight

            else:
                dist_row.append(math.inf)        # no direct edge

            col = col + 1

        dist.append(dist_row)
        row = row + 1

    return dist


def initialize_next(n):
    next_node = []
    row       = 0

    while row < n:
        next_row = []
        col      = 0

        while col < n:
            if row != col:
                next_row.append(col)    # initially go directly to destination
            else:
                next_row.append(-1)     # no path to self
            col = col + 1

        next_node.append(next_row)
        row = row + 1

    return next_node


def floyd_warshall(graph):
    n         = len(graph)
    dist      = initialize_dist(graph, n)
    next_node = initialize_next(n)

    # Try every node as an intermediate
    k = 0
    while k < n:
        i = 0

        while i < n:
            j = 0

            while j < n:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j]      = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]   # route through k

                j = j + 1
            i = i + 1
        k = k + 1

    # Negative cycle detection
    # If dist[i][i] < 0, node i is part of a negative cycle
    i = 0
    while i < n:
        if dist[i][i] < 0:
            return None, None       # negative cycle detected
        i = i + 1

    return dist, next_node


# ─────────────────────────────────────────
# PATH RECONSTRUCTION
# ─────────────────────────────────────────

def get_path(next_node, source, destination):
    if next_node[source][destination] == -1:
        return []               # no path exists

    path    = [source]
    current = source

    while current != destination:
        current = next_node[current][destination]
        path.append(current)

    return path


# ─────────────────────────────────────────
# PRINT HELPERS
# ─────────────────────────────────────────

def print_dist_matrix(dist, n):
    print("Shortest distance matrix:")
    print("      ", end="")

    col = 0
    while col < n:
        print("  {:>6}".format(col), end="")
        col = col + 1
    print()

    row = 0
    while row < n:
        print("Node", row, end="")
        col = 0
        while col < n:
            if dist[row][col] == math.inf:
                print("     INF", end="")
            else:
                print("  {:>6}".format(dist[row][col]), end="")
            col = col + 1
        print()
        row = row + 1


def print_all_paths(dist, next_node, n):
    print("All pairs shortest paths:")
    src = 0

    while src < n:
        dst = 0

        while dst < n:
            if src != dst:
                path = get_path(next_node, src, dst)

                if not path:
                    print("  ", src, "→", dst, ": NO PATH")
                else:
                    index        = 0
                    path_string  = ""

                    while index < len(path):
                        if index < len(path) - 1:
                            path_string = path_string + str(path[index]) + " → "
                        else:
                            path_string = path_string + str(path[index])
                        index = index + 1

                    print("  ", src, "→", dst, ":  path =", path_string, "  dist =", dist[src][dst])

            dst = dst + 1
        src = src + 1


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == '__main__':

    # Directed weighted graph
    # 0 = no direct edge
    #
    #   0 --(3)--> 1 --(1)--> 3
    #   |          |
    #  (8)        (4)
    #   |          |
    #   ▼          ▼
    #   2 --(2)--> 4
    #   ▲          |
    #   └───(1)────┘

    graph = [
        [0, 3, 8, 0, 0],   # Node 0
        [0, 0, 0, 1, 4],   # Node 1
        [0, 0, 0, 0, 0],   # Node 2
        [0, 0, 0, 0, 0],   # Node 3
        [0, 0, 1, 0, 0]    # Node 4
    ]

    n = len(graph)

    dist, next_node = floyd_warshall(graph)

    if dist is None:
        print("Negative cycle detected!")
    else:
        print("=== Floyd-Warshall ===")
        print()
        print_dist_matrix(dist, n)
        print()
        print_all_paths(dist, next_node, n)

    print()

    # Negative cycle demo
    print("=== Negative Cycle Detection ===")

    graph_neg_cycle = [
        [0, 1,  0],   # Node 0
        [0, 0, -3],   # Node 1
        [2, 0,  0]    # Node 2  →  0→1→2→0 = 1 + (−3) + 2 = −1 cycle
    ]

    dist, next_node = floyd_warshall(graph_neg_cycle)

    if dist is None:
        print("Negative cycle detected!")
    else:
        print_dist_matrix(dist, len(graph_neg_cycle))