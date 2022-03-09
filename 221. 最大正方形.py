# Given an m x n binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for i in range(m + 1)]  # 以i, j结尾的最短的边全是1（才能构成正方形）
        result = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '0':
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                result = max(result, dp[i][j])
        return result ** 2