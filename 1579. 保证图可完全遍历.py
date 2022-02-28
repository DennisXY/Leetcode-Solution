# Alice and Bob have an undirected graph of n nodes and 3 types of edges:
#
# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can by traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi]
# represents a bidirectional edge of type typei between nodes ui and vi,
# find the maximum number of edges you can remove so that after removing the edges,
# the graph can still be fully traversed by both Alice and Bob.
# The graph is fully traversed by Alice and Bob if starting from any node,
# they can reach all other nodes.
#
# Return the maximum number of edges you can remove,
# or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

#https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class DisjointSetUnion:
    def __init__(self, M):
        self.parent = {}
        self.cnt = M

        for i in range(1, M + 1):
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        Alice = DisjointSetUnion(n)
        Bob = DisjointSetUnion(n)
        result = 0
        edges.sort(reverse=True)
        for edge in edges:
            x, y = edge[1], edge[2]
            if edge[0] == 3:
                if not Alice.connected(x, y):
                    Alice.union(x, y)
                    Bob.union(x, y)
                else:
                    #alice connected by the public line, so we can remove the Alice line
                    result += 1
            else:
                if Alice.connected(x, y) and Bob.connected(x, y):
                    result += 1
                    continue
                if edge[0] == 1:
                    if Alice.connected(x, y):
                        result += 1
                        continue
                    Alice.union(x, y)
                else:
                    if Bob.connected(x, y):
                        result += 1
                        continue
                    Bob.union(x, y)

        if Alice.cnt * Bob.cnt > 1:
            return -1

        return result