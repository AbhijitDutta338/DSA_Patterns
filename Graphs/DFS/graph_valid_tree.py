def validTree(self, n, edges):
    if not n:
        return True
    #Create Adjacency List
    adj = { i: [] for i in range(n) }
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit = set()
    #dfs to check if its having a cycle or not
    def dfs(i, prev):
        if i in visit:
            return False
        visit.add(i)
        
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j, i):
                return False
        return True

    # if len(visit) == n: it means all nodes are connected
    # dfs to check if graph is not having a cycle
    # if both are true, its a tree
    return dfs(0, -1) and n == len(visit)