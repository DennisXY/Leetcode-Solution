# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
#  
#
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]

        if m * n == 0:
            return m + n

        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                down = dp[i - 1][j] + 1
                right = dp[i][j - 1] + 1
                if word1[i - 1] != word2[j - 1]:
                    down_right = dp[i - 1][j - 1] + 1
                else:
                    down_right = dp[i - 1][j - 1]
                dp[i][j] = min(down, right, down_right)
        return dp[m][n]