# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
# |xi - xj| + |yi - yj|,
# where |val| denotes the absolute value of val.
#
# Return the minimum cost to make all points connected. All points are connected
# if there is exactly one simple path between any two points.

class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret