class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    def find(self, x):
        pass
    def union(self, x, y):
        pass

def kruskal(n, edges):
    edges = [(u, v, weight), ...]  # list of edges in the graph
    edges.sort(key=lambda x: x[2])  # sort by weight
    mst = []
    uf = UnionFind(n)

    for edge in edges:
        u, v, weight = edge
        # Only add edge if it connects two different components (no cycle)
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append(edge)

        if len(mst) == n - 1:
            break

    return mst  