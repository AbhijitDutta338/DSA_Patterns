class Solution:
    # Solution class wrapper (LeetCode-style)
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Compute largest rectangle area in a histogram.
        # `heights` is a list of bar heights.
        stack = []  # stores indices of bars with increasing heights
        max_area = 0  # tracks the maximum area found

        heights.append(0)  # sentinel: append zero to flush remaining bars at end

        for i, h in enumerate(heights):
            # For each bar, when current height is lower than stack top,
            # we've found the right boundary for taller bars on the stack.
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # height of the bar being finalized
                right = i  # exclusive right boundary for this bar's maximal rectangle
                left = stack[-1] if stack else -1  # index of previous smaller bar, -1 if none
                width = right - left - 1  # width the bar can span
                max_area = max(max_area, height * width)  # update max_area if larger

            stack.append(i)  # push current index to maintain increasing-height stack

        return max_area  # largest rectangle area