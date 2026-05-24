## Check if a graph is bipartite using BFS
n = 10  # number of vertices in the graph
color = [-1] * n  # uncolored

def isBipartite(start):
    queue = [start]
    color[start] = 0

    while queue: #is not empty
        node = queue.pop()
        for neighbor in node.neighbors:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                queue.push(neighbor)
            elif color[neighbor] == color[node]:
                return False

    return True