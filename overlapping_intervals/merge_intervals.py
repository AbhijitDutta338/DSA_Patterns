'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        result = []
        currentStart = intervals[0][0]
        currentEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start <= currentEnd:
                if end > currentEnd:
                    currentEnd = end
            else:
                result.append([currentStart, currentEnd])
                currentStart = start
                currentEnd = end

        result.append([currentStart, currentEnd])
        return result