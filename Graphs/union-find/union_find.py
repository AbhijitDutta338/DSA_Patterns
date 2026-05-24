'''
Given n nodes and a list of edges, support two operations efficiently:
- union(a, b): connect nodes a and b
- find(a):     find the root/representative of a's component

Applications: detect cycles, count connected components, MST (Kruskal's)
'''
n = 10  # example number of nodes
parent = [0, 1, 2, ..., n-1]  # each node is its own leader
rank = [0] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return False  # already connected

    # Union by rank: attach smaller tree to root of larger tree
    if rank[px] < rank[py]:
        parent[px] = py
    elif rank[px] > rank[py]:
        parent[py] = px
    else: # Ranks are equal; choose one as new root and increment its rank
        parent[py] = px
        rank[px] += 1

    return True