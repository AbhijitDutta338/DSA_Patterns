'''
Given a directed graph of n nodes and directed edges,
produce a linear ordering where for every edge u→v, u comes before v.

Goal: Topological sort. If a cycle exists, it's impossible — return [].

Applications: task scheduling, build order, course prerequisites
'''
from collections import deque

class Solution:
    def topoSort(self, n: int, edges: list[tuple[int, int]]) -> list[int]:
        # Build adjacency list and track in-degrees
        adj     = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1  # v has one more prerequisite

        # Start with all nodes that have no prerequisites
        queue = deque()
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            # "Remove" this node: reduce in-degree of its neighbors
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:  # all prerequisites met
                    queue.append(neighbor)

        # If not all nodes are in order, a cycle exists
        return order if len(order) == n else []


# --- Usage ---
# n = 6, edges = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
# topoSort(n, edges) → [4, 5, 0, 2, 1, 3]  (one valid ordering)