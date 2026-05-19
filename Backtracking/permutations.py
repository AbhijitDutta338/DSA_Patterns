class Solution(object):
    def permutations(self, nums):
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
           
            for num in nums:
                # Skip if the number is already in the current path to avoid duplicates
                if num in path:
                    continue

                # Include the current number and move to the next index
                path.append(num)
                backtrack(path)
                # Backtrack: remove the last number to explore the next possibility
                path.pop()

        backtrack([])
        return result