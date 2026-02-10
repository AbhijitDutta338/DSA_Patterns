#Topological Sort using DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses
        order = []
        self.hasCycle = False

        for i in range(numCourses):
            if state[i] == 0:
                self.dfs(i, graph, state, order)
                if self.hasCycle:
                    return []

        order.reverse()
        return order

    def dfs(self, node: int, graph: list[list[int]], state: list[int], order: list[int]) -> None:
        if self.hasCycle:
            return

        state[node] = 1  # visiting

        for neighbor in graph[node]:
            if state[neighbor] == 0:
                self.dfs(neighbor, graph, state, order)
            elif state[neighbor] == 1:
                self.hasCycle = True
                return

        state[node] = 2  # visited
        order.append(node)
