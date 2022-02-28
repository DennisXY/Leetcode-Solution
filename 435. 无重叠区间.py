# Given a collection of intervals,
# find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Example 1:
#
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
#
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
#
# Input: [[1,2],[2,3]]
# Output: 0
#
# Note:
#
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

class Solution:
    def eraseOverlapIntervals(self, intervals):
        def sort_index(item):
            return item[1]
        intervals.sort(key=sort_index)
        cur_inx = 0
        result = 0
        total_length = len(intervals)
        while cur_inx < total_length - 1:
            if intervals[cur_inx][1] <= intervals[cur_inx + 1][0]:
                cur_inx += 1
                continue
            else:
                intervals.remove(intervals[cur_inx + 1])
                total_length -= 1
                result += 1
        return result


if __name__ == '__main__':
    a = [[1,2],[2,3],[3,4],[1,3]]
    solution = Solution()
    x = solution.eraseOverlapIntervals(a)
    print(x)