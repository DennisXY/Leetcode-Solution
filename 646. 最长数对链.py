# You are given n pairs of numbers. In every pair,
# the first number is always smaller than the second number.
#
# Now, we define a pair (c, d) can follow another pair (a, b)
# if and only if b < c. Chain of pairs can be formed in this fashion.
#
# Given a set of pairs, find the length longest chain which can be formed.
# You needn't use up all the given pairs. You can select pairs in any order.
#
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].

class Solution:
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)


if __name__ == '__main__':
    a = [[1,2], [2,4], [2, 3]]
    solution = Solution()
    c = solution.findLongestChain(a)
    print(c)