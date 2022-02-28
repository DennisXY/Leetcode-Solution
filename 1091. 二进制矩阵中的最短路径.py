# In an N by N square grid, each cell is either empty (0) or blocked (1).
#
# A clear path from top-left to bottom-right has length k if and only if
# it is composed of cells C_1, C_2, ..., C_k such that:
#
# Adjacent cells C_i and C_{i+1} are connected 8-directionally
# (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.
# If such a path does not exist, return -1.

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1
        res = 1
        path = deque()
        path.append([0, 0])
        while path:  # BFS模板
            for _ in range(len(path)):  # 对BFS的某一层的中所有点向8个方向进行扩展
                x, y = path.popleft()
                for new_x, new_y in [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1],
                                     [x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]:
                    # 下面几种continue可以合并一行，这里为看的清楚就分开写了
                    if new_x == n - 1 and new_y == n - 1:  # 如果扩展的点到达了终点
                        return res + 1
                    if not 0 <= new_x < n or not 0 <= new_y < n:  # 扩展的点超出边界，则跳过
                        continue
                    if grid[new_x][new_y] == 1:  # 若扩展的点为阻塞，则跳过
                        continue
                    if grid[new_x][new_y] == -1:  # 若扩展的点已经访问过，则跳过
                        continue
                    if grid[new_x][new_y] == 0:  # 若为通畅点
                        grid[new_x][new_y] = -1  # 当前层次下已经访问该点
                        path.append([new_x, new_y])  # 将扩展的点加入path，到下一层的时候继续扩展
            res += 1  # 对某一层的元素都求判定过后，距离加1(同一个层次中的所有点的距离距离起点都是相等的）
        return -1