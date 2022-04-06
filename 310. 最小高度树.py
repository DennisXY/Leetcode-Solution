# A tree is an undirected graph in which any two vertices are connected by
# exactly one path. In other words, any connected graph without
# simple cycles is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 
# edges where edges[i] = [ai, bi] indicates that there is an undirected edge
# between the two nodes ai and bi in the tree, you can choose any node of the
# tree as the root. When you select a node x as the root, the result tree has
# height h. Among all possible rooted trees, those with minimum height
# (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.

# 着重是数学证明，看官方题解
# https://leetcode-cn.com/problems/minimum-height-trees/solution/zui-xiao-gao-du-shu-by-leetcode-solution-6v6f/

# 只需要求出路径最长的两个叶子节点即可，并求出其路径的最中间的节点即为最小高度树的
# 根节点。可以利用以下算法找到图中距离最远的两个节点与它们之间的路径

from collections import *


class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]