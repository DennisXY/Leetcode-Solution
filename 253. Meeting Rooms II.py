# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of conference rooms required.

# Example 1:
#
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
#
# Input: intervals = [[7,10],[2,4]]
# Output: 1

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()

        free_rooms = list()

        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0

        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        end_pointer = 0
        start_pointer = 0

        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1
            start_pointer += 1

        return used_rooms