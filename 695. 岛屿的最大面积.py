# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11,
# because the island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        island = deque()
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                island.append([i, j])
                temp = 0
                while island:
                    x, y = island.popleft()
                    if grid[x][y] == 0:
                        continue
                    temp += 1
                    grid[x][y] = 0
                    for newX, newY in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                        if not 0 <= newX < m or not 0 <= newY < n:
                            continue
                        if grid[newX][newY] == 0:
                            continue
                        island.append([newX, newY])
                res = max(temp, res)
        return res