# ─────────────────────────────────────────
# UNION FIND  (Disjoint Set Union — DSU)
# ─────────────────────────────────────────
# Supports two operations:
#   find(x)        — which group does x belong to?
#   union(x, y)    — merge the groups of x and y
#
# Optimizations:
#   Path Compression  — flatten tree during find
#   Union by Rank     — always attach smaller tree under larger

def make_set(n):
    parent = list(range(n))     # each node is its own parent initially
    rank   = [0] * n            # rank (tree height) starts at 0
    return parent, rank


def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])   # path compression
    return parent[node]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return False            # already in the same group — no merge needed

    # Union by rank — attach smaller tree under larger
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y

    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x

    else:
        parent[root_y] = root_x
        rank[root_x]   = rank[root_x] + 1

    return True                 # merge happened


def is_connected(parent, x, y):
    return find(parent, x) == find(parent, y)


# ─────────────────────────────────────────
# PRINT HELPER
# ─────────────────────────────────────────

def print_groups(parent, n):
    groups = {}
    index  = 0

    while index < n:
        root = find(parent, index)
        if root not in groups:
            groups[root] = []
        groups[root].append(index)
        index = index + 1

    print("Groups:")
    for root, members in groups.items():
        print("  Root", root, "→", members)


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == '__main__':

    # ── Basic Union Find ──────────────────
    print("=== Basic Union Find ===")
    print()

    n = 7
    parent, rank = make_set(n)

    print("Initial state — every node is its own group:")
    print_groups(parent, n)
    print()

    print("union(0, 1):", union(parent, rank, 0, 1))
    print("union(1, 2):", union(parent, rank, 1, 2))
    print("union(3, 4):", union(parent, rank, 3, 4))
    print("union(5, 6):", union(parent, rank, 5, 6))
    print("union(0, 4):", union(parent, rank, 0, 4))
    print()

    print("After unions:")
    print_groups(parent, n)
    print()

    print("is_connected(0, 3):", is_connected(parent, 0, 3))   # True  — merged via 0→1→2, 3→4, 0→4
    print("is_connected(0, 5):", is_connected(parent, 0, 5))   # False — group 5,6 is separate
    print("is_connected(5, 6):", is_connected(parent, 5, 6))   # True  — directly merged
    print()

    # ── Cycle Detection ───────────────────
    print("=== Cycle Detection in a Graph ===")
    print()

    # edges of an undirected graph
    # union returns False if both nodes already share a root → cycle!

    edges_no_cycle = [
        (0, 1),
        (1, 2),
        (2, 3)
    ]

    edges_with_cycle = [
        (0, 1),
        (1, 2),
        (2, 0)      # this creates a cycle
    ]

    parent, rank = make_set(4)
    cycle_found  = False
    index        = 0

    while index < len(edges_no_cycle):
        u, v = edges_no_cycle[index]
        if not union(parent, rank, u, v):
            cycle_found = True
        index = index + 1

    print("Graph without cycle — cycle detected?", cycle_found)

    parent, rank = make_set(4)
    cycle_found  = False
    index        = 0

    while index < len(edges_with_cycle):
        u, v = edges_with_cycle[index]
        if not union(parent, rank, u, v):
            cycle_found = True
        index = index + 1

    print("Graph with cycle    — cycle detected?", cycle_found)
    print()

    # ── Connected Components ──────────────
    print("=== Connected Components ===")
    print()

    # How many separate islands exist in this graph?
    #
    #   0 — 1    2 — 3    4
    #   (group1) (group2) (group3 — isolated)

    n     = 5
    edges = [(0, 1), (2, 3)]

    parent, rank = make_set(n)
    index        = 0

    while index < len(edges):
        u, v = edges[index]
        union(parent, rank, u, v)
        index = index + 1

    print_groups(parent, n)

    components = set()
    index      = 0
    while index < n:
        components.add(find(parent, index))
        index = index + 1

    print("Number of connected components:", len(components))
    print()

    # ── Kruskal's MST using Union Find ────
    print("=== Kruskal's MST using Union Find ===")
    print()

    # Kruskal's builds MST by greedily picking cheapest edge
    # that does NOT form a cycle — union find detects the cycle

    #   0 --(1)-- 1 --(4)-- 2
    #   |         |         |
    #  (3)       (2)       (5)
    #   |         |         |
    #   3 --(6)-- 4 --(7)-- 5

    n            = 6
    parent, rank = make_set(n)

    # (weight, u, v) — sorted by weight ascending
    weighted_edges = [
        (1, 0, 1),
        (2, 1, 4),
        (3, 0, 3),
        (4, 1, 2),
        (5, 2, 5),
        (6, 3, 4),
        (7, 4, 5)
    ]

    mst_edges  = []
    mst_cost   = 0
    index      = 0

    while index < len(weighted_edges):
        weight, u, v = weighted_edges[index]

        if union(parent, rank, u, v):       # no cycle — safe to add
            mst_edges.append((u, v, weight))
            mst_cost = mst_cost + weight

        index = index + 1

    print("MST edges:")
    edge_index = 0
    while edge_index < len(mst_edges):
        u, v, w = mst_edges[edge_index]
        print("  Node", u, "--(" , w , ")--> Node", v)
        edge_index = edge_index + 1

    print("MST total cost:", mst_cost)