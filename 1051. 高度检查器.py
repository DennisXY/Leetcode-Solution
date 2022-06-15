# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order
# by height. Let this ordering be represented by the integer array expected
# where expected[i] is the expected height of the ith student in line.
#
# You are given an integer array heights representing the current order that
# the students are standing in. Each heights[i] is the height of the ith student
# in line (0-indexed).
#
# Return the number of indices where heights[i] != expected[i].
#
# Example 1:
#
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.
# 笨办法：排序之后一一比对相加
# 新办法：因为数组比较小，可以使用计数排序


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        Max = max(heights)
        cnt = [0] * (Max + 1)

        for height in heights:
            cnt[height] += 1

        idx, ans = 0, 0

        for i in range(1, Max + 1):
            for j in range(cnt[i]):
                if heights[idx] != i:
                    ans += 1
                idx += 1
        return ans