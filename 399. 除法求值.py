# You are given an array of variable pairs equations and an array of real numbers values,
# where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
# Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj]
# represents the jth query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid.
# You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

#
# Example 1:
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# Example 2:
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:
#
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]

# https://leetcode-cn.com/problems/evaluate-division/solution/399-chu-fa-qiu-zhi-nan-du-zhong-deng-286-w45d/

class UnionFind:
    def __init__(self):
        """
        记录每个节点的父节点
        记录每个节点到根节点的权重
        """
        self.father = {}
        self.value = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        更新权重
        """
        root = x
        # 节点更新权重的时候要放大的倍数
        base = 1
        while self.father[root] != None:
            root = self.father[root]
            base *= self.value[root]

        while x != root:
            original_father = self.father[x]
            ##### 离根节点越远，放大的倍数越高
            self.value[x] *= base
            base /= self.value[original_father]
            #####
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y, val):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            ##### 四边形法则更新根节点的权重
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self, x, y):
        """
        两节点是否相连
        """
        return x in self.value and y in self.value and self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点，初始化权重为1.0
        """
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)

        res = [-1.0] * len(queries)

        for i, (a, b) in enumerate(queries):
            if uf.is_connected(a, b):
                res[i] = uf.value[a] / uf.value[b]
        return res