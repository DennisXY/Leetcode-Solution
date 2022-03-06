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


class Solution:
    def numIslands(self, grid) -> int:
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n, result = len(grid), len(grid[0]), 0

        island = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                result += 1
                island.append([i, j])
                while island:
                    x, y = island.pop(0)
                    if grid[x][y] == '0':
                        continue
                    grid[x][y] = '0'
                    for newX, newY in move:
                        if not 0 <= x+newX < m or not 0 <= y+newY < n:
                            continue
                        if grid[x+newX][y+newY] == '0':
                            continue
                        island.append([x+newX, y+newY])
        return result