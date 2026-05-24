'''
Topological Sort algorithm is used to order the vertices of a Directed Acyclic Graph (DAG) in a linear sequence, 
such that for every directed edge u → v, vertex u comes before vertex v in the ordering.
'''

def topological_sort_dfs(graph):
    visited = set()
    ordering = []

    def dfs(vertex):
        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        
        ordering.append(vertex) #post ordering in graph. <Ensures all dependencies are added last in reverse>

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    return ordering[::-1]  # Reverse the ordering array to get the correct order of tasks