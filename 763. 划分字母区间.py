# A string S of lowercase English letters is given.
# We want to partition this string into as many parts as possible so that
# each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
#
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.

class Solution:
    def partitionLabels(self, S):

        intervals = []
        result = []
        length = len(S)
        if length == 0:
            return 0
        # 得到每个字母的区间
        for s in set(S):
            intervals.append([S.find(s), S.rfind(s)])

        ## 根据区间的左端点排序
        intervals.sort(key=lambda x: x[0])

        last_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] - 1 >= last_interval[1]: #此时区间不重叠，可以分隔开
                result.append(intervals[i][0] - last_interval[0])
                last_interval = intervals[i]
            else:
                last_interval[1] = max(last_interval[1], intervals[i][1]) #不重叠，取最大的右侧

        result.append(length - sum(result))
        return result


if __name__ == '__main__':
    a = "ababcbacadefegdehijhklij"
    solution = Solution()
    c = solution.partitionLabels(a)
    print(c)