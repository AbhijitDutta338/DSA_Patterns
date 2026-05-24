##Undirected graph
'''
For undirected graphs: if you reach a visited node that isn’t your immediate parent, you’ve found a cycle.
'''
def hasCycle(node, parent, visited):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if hasCycle(neighbor, node, visited):  # current node becomes parent
                return True
        elif neighbor != parent:   # visited AND not my parent → cycle
            return True

    return False

#Directed graph cycle detection
'''
For directed graphs: you use three states (unvisited, in-progress, completed). If you reach an in-progress node, you’ve found a back edge, which means a cycle.
'''

UNVISITED, IN_PROGRESS, COMPLETED = 0, 1, 2
state = [UNVISITED] * n

def hasCycle(node):
    state[node] = IN_PROGRESS        # entering → add to current path

    for neighbor in graph[node]:
        if state[neighbor] == IN_PROGRESS:
            return True              # back edge → cycle found
        if state[neighbor] == UNVISITED:
            if hasCycle(neighbor):
                return True
        # COMPLETED → skip, already verified no cycle through it

    state[node] = COMPLETED          # exiting → remove from current path
    return False