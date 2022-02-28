# You are a hiker preparing for an upcoming hike.
# You are given heights, a 2D array of size rows x columns,
# where heights[row][col] represents the height of cell (row, col).
# You are situated in the top-left cell, (0, 0),
# and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,0-indexed).
# You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

class DisjointSetUnion:
    def __init__(self, M):
        self.parent = {}
        self.cnt = M
        for i in range(M):
            self.parent[i] = i

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.connected(x, y): return
        parent_x = self.find(x)
        parent_y = self.find(y)
        self.parent[parent_x] = parent_y
        self.cnt -= 1


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        edges = list()
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append((iden - n, iden, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((iden - 1, iden, abs(heights[i][j] - heights[i][j - 1])))
        edges.sort(key=lambda e: e[2])

        uf = DisjointSetUnion(m * n)
        ans = 0
        for x, y, v in edges:
            uf.union(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break
        return ans
