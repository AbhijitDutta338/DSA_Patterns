class Solution(object):
    def combinations(self, n, k):
        result = []

        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for num in range(start, n + 1):
                # Include the current number 
                path.append(num)
                backtrack(num + 1, path)
                # Backtrack: remove the last number to explore the next possibility
                path.pop()

        backtrack(1, [])
        return result