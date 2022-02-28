# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
# there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the
# range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

# 我们可以将四个数组分成两部分，A 和 B为一组，C 和 D 为另外一组。
#
# 对于 A 和 B，我们使用二重循环对它们进行遍历，得到所有 A[i]+B[j]的值并存入哈希映射中。
# 对于哈希映射中的每个键值对，每个键表示一种 A[i]+B[j]，对应的值为 A[i]+B[j] 出现的次数。
#
# 对于 C 和 D，我们同样使用二重循环对它们进行遍历。当遍历到 C[k]+D[l]时，如果 -(C[k]+D[l])
# 出现在哈希映射中，那么将 -(C[k]+D[l])对应的值累加进答案中。
#
# 最终即可得到满足 A[i]+B[j]+C[k]+D[l]=0的四元组数目。


import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = collections.Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans

