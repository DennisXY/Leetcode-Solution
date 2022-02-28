# Given an array, strs, consisting of only 0s and 1s. Also two integers m and n.
#
# Find the maximum number of strings that you can form with given m 0s and n 1s.
# Each 0 and 1 can be used at most once.
#
# Example 1:
#
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s
# which are "10","0001","1","0".
# Example 2:
#
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".


class Solution:
    def findMaxForm(self, strs, m, n):
        length = len(strs)
        dp = [[0] * (n+1) for i in range(m+1)]

        for str in strs:
            count_0 = str.count('0')
            count_1 = str.count('1')

            for i in range(m, count_0 - 1, -1):
                for j in range(n, count_1 - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - count_0][j - count_1])
        return dp[m][n]

if __name__ == '__main__':
    a = ["10","0001","111001","1","0"]
    # solution = Solution()
    # c = solution.validPalindrome(a)

    print(a)