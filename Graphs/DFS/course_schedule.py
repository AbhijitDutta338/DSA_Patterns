'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
The pair [0, 1], indicates that must take course 1 before taking course 0.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        UNVISITED, IN_PROGRESS, COMPLETED = 0, 1, 2
        state = [UNVISITED] * numCourses

        graph = {u:[] for u in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        #dfs to find cycle

        def hasCycle(node):
            state[node] = IN_PROGRESS        # entering → add to current path

            for neighbor in graph[node]:
                if state[neighbor] == IN_PROGRESS:
                    return True              # back edge → cycle found
                if state[neighbor] == UNVISITED:
                    if hasCycle(neighbor):
                        return True

            state[node] = COMPLETED          # exiting → remove from current path
            return False
        
        for u in range(numCourses):
            if hasCycle(u): return False
        
        return True