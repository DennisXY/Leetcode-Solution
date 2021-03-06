# A binary string is monotone increasing if it consists of some number of 0's
# (possibly none), followed by some number of 1's (also possibly none).
#
# You are given a binary string s. You can flip s[i] changing it from 0 to 1
# or from 1 to 0.
#
# Return the minimum number of flips to make s monotone increasing.
#
# Example 1:
#
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
# 动态规划


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for c in s:
            dp0New, dp1New = dp0, min(dp0, dp1)
            if c == '1':
                dp0New += 1
            else:
                dp1New += 1
            dp0, dp1 = dp0New, dp1New
        return min(dp0, dp1)
