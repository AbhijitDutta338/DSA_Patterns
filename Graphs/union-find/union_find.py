'''
Given n nodes and a list of edges, support two operations efficiently:
- union(a, b): connect nodes a and b
- find(a):     find the root/representative of a's component

Applications: detect cycles, count connected components, MST (Kruskal's)
'''
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))  # each node is its own parent initially
        self.rank   = [0] * n         # rank: tree height estimate for union by rank

    def find(self, x: int) -> int:
        # Path compression: point every node directly to root on the way up
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False  # already in same component (edge is a cycle)

        # Union by rank: attach smaller tree under larger tree
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1  # only grows when ranks are equal

        return True  # successfully merged two components

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


# --- Usage ---
# uf = UnionFind(5)
# uf.union(0, 1)
# uf.union(1, 2)
# uf.connected(0, 2) → True
# uf.union(3, 4)
# uf.connected(0, 3) → False