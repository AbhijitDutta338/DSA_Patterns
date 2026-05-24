from collections import deque

def topological_sort_kahn(graph):
    in_degree = {u: 0 for u in graph}

    #calculate indegree - no of incoming edges to a node (u->v)
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    #Enqueue only those nodes that has 0 indegree - meaning no dependent actions
    queue = deque([u for u in in_degree if in_degree[u] == 0])
    topo_order = []

    #Do BFS
    while queue:
        u = queue.popleft()
        topo_order.append(u) # add indegree 0 node to the path as all dependencies are over.

        for v in graph.get(u, []):
            #reduce indegree of neighbors
            in_degree[v] -= 1
            #Enqueue neighbors with 0 indegree
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) == len(in_degree):
        return topo_order
    else:
        raise Exception("Graph has at least one cycle")