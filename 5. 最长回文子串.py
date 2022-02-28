# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length, max_length, res = len(s), 0, s[0]
        dp = [[True] * length for i in range(length)]
        for i in range(1, length):
            for j in range(i):
                dp[i][j] = dp[i-1][j+1] and s[i] == s[j]
                if dp[i][j]:
                    if max_length < i-j+1:
                        max_length = i-j+1
                        res = s[j:i+1]
        return res
