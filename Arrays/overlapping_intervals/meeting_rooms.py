'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])

        previousEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < previousEnd:
                return False

            previousEnd = end

        return True