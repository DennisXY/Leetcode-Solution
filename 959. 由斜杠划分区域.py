# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or
# blank space. These characters divide the square into contiguous regions.
#
# (Note that backslash characters are escaped, so a \is represented as "\\".)
#
# Return the number of regions.

#answer
# https://leetcode-cn.com/problems/regions-cut-by-slashes/solution/liang-chong-fang-fa-bing-cha-ji-he-dfs95-uhof/

class DisjointSetUnion:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0

        for i in range(M):
            self.parent[i] = i
            self.cnt += 1

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
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        N = n * n * 4
        uf = DisjointSetUnion(N)

        def get_pos(row, col, i):
            return (row * n + col) * 4 + i

        for row in range(n):
            for col in range(n):
                v = grid[row][col]
                if row > 0:
                    uf.union(get_pos(row - 1, col, 2), get_pos(row, col, 1))
                if col > 0:
                    uf.union(get_pos(row, col - 1, 3), get_pos(row, col, 0))
                if v == '/':
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 1))
                    uf.union(get_pos(row, col, 2), get_pos(row, col, 3))
                if v == '\\':
                    uf.union(get_pos(row, col, 1), get_pos(row, col, 3))
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 2))
                if v == ' ':
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 1))
                    uf.union(get_pos(row, col, 1), get_pos(row, col, 2))
                    uf.union(get_pos(row, col, 2), get_pos(row, col, 3))
        return uf.cnt

