def dfs(node, visited):
    if node in visited:
        return

    #add current node to visited
    visited.add(node)

    #Go in depth on each neighbor
    for neighbor in node.neighbors:
        dfs(neighbor, visited)


#Iterative:
def dfs_iterative(graph, start):
    visited = set()
    #Use stack to maintain recursive call loop.
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(f"Visiting {node}")
            # Add neighbors to stack
            stack.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
    return visited