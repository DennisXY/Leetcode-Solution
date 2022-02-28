# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#  
#
# Example 1:
#
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Example 2:
#
# Input: s = "a"
# Output: 0
# Example 3:
#
# Input: s = "ab"
# Output: 1

class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        dp = [[True] * length for i in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        f = [100000 for i in range(length)]
        for i in range(length):
            if dp[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        f[i] = min(f[j] + 1, f[i])
        return f[-1]
