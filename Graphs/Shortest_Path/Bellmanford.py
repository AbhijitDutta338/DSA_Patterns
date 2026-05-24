def bellman_ford(graph, start):
    # graph: list of edges [(u, v, weight), ...]
    num_vertices = len({u for edge in graph for u in edge[:2]})
    distances = {vertex: float('inf') for edge in graph for vertex in edge[:2]}
    distances[start] = 0

    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            raise Exception("Graph contains a negative-weight cycle")

    return distances