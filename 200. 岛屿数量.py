# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        island = deque()
        res = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = int(grid[i][j])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += 1
                island.append([i, j])
                while island:
                    x, y = island.popleft()
                    if grid[x][y] == 0:
                        continue
                    grid[x][y] = 0
                    for newX, newY in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                        if not 0 <= newX < m or not 0 <= newY < n:
                            continue
                        if grid[newX][newY] == 0:
                            continue
                        island.append([newX, newY])

        return res