# Given a positive integer n,
# find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:
    def numSquares(self, n) -> int:
        if n == 1:
            return 1
        square_nums = [i**2 for i in range(0, int(n/2)+1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]

if __name__ == '__main__':
    a = 12
    solution = Solution()
    c = solution.numSquares(a)
    print(c)