# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected directly with city c,
# then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities
# outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city
# and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1

        return circles