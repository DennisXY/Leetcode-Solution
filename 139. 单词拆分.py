# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        length = len(s)
        dp = [False] * (length+1)
        dp[0] = True
        for i in range(length+1):
            for j in range(i, length+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

