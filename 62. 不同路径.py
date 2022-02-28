# A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28

class Solution:
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        if m == 0 or n == 0:
            return 1
        matrix = [[1 for i in range(n)] for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]
if __name__ == '__main__':
    a = 1
    b = 1
    solution = Solution()
    b = solution.uniquePaths(a, b)
    print(b)
