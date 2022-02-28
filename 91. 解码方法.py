# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation:It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution:
    def numDecodings(self, s):
        if s.startswith('0'):  # 开头有 ‘0’ 直接返回
            return 0

        n = len(s)
        dp = [1] * (n + 1)  # 重点是 dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            if s[i - 1] == '0' and s[i - 2] not in '12':  # 出现前导 ‘0’ 的情况，不能解码，直接返回
                return 0
            if s[i - 2:i] in ['10', '20']:  # 只有组合在一起才能解码
                dp[i] = dp[i - 2]
            elif '10' < s[i - 2:i] <= '26':  # 两种解码方式
                dp[i] = dp[i - 1] + dp[i - 2]
            else:  # '01'到 ‘09’ 或 > '26'，只有单独才能解码
                dp[i] = dp[i - 1]
        return dp[n]

if __name__ == '__main__':
    a = "1212"
    solution = Solution()
    c = solution.numDecodings(a)
    print(c)