# Given two strings text1 and text2,
# return the length of their longest common subsequence. If there is no common subsequence, return 0.
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        str1, str2 = text1, text2
        dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


# Second Version: The substring should be continuous
# 输入："1AB2345CD","12345EF"
# 返回值："2345"
# 返回字符串，而不是数字

class Solution:
    def LCS(self, str1, str2):
        max_result = ""
        dp = [[""] * (len(str2) + 1) for i in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                    if len(max_result) < len(dp[i][j]):
                        max_result = dp[i][j]
                else:
                    dp[i][j] = ""

        return max_result