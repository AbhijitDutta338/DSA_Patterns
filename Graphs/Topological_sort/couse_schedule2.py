'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.
'''

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {u: [] for u in range(numCourses)}

        #Create the Adjacency List
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        
        #Khan's Algo - Topological sort with BFS
        in_degree = {u: 0 for u in range(numCourses)}

        #calculate indegree
        for u in range(numCourses):
            for v in graph[u]:
                in_degree[v] = in_degree.get(v, 0) + 1

        #Enqueue nodes with 0 indegree 
        queue = deque([u for u in in_degree if in_degree[u] == 0])
        topo_order = []

        #Do BFS
        while queue:
            u = queue.popleft()
            topo_order.append(u) # add indegree 0 node to the path 

            for v in graph.get(u, []):
                #reduce indegree of neighbors
                in_degree[v] -= 1
                #Enqueue neighbors with 0 indegree
                if in_degree[v] == 0:
                    queue.append(v)

        if len(topo_order) == len(in_degree):
            return topo_order
        else:
            return []