class Solution(object):
    def subsets(self, nums):
        result = []

        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            # Include the current number
            path.append(nums[index])
            backtrack(index + 1, path)

            #go back and remove the current number to explore the next possibility
            path.pop()

            # Exclude the current number
            backtrack(index + 1, path)

        backtrack(0, [])
        return result