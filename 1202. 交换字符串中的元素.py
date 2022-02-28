# You are given a string s, and an array of pairs of indices in the string pairs
# where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
# You can swap the characters at any pair of indices in the given pairs any number of times.
#
# Return the lexicographically smallest string that s can be changed to after using the swaps.
#
# Example 1:
#
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:
#
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:
#
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"

#根据pairs对索引建图，可以用字典也可以用数组。然后采用DFS获取每一块连通分量的索引，再排序赋值即可。
class Solution:
    def dfs(self, res, graph, visited, x):
        for neighbor in graph[x]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                res.append(neighbor)
                self.dfs(res, graph, visited, neighbor)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = [[] for i in range(len(s))]
        visited = [False] * len(s)
        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)
        res = list(s)
        for i in range(len(s)):
            if not visited[i]:
                connected_nodes = list()
                self.dfs(connected_nodes, graph, visited, i)
                indices = sorted(connected_nodes)
                string = sorted(res[node] for node in connected_nodes)
                for j, ch in zip(indices, string):
                    res[j] = ch

        return "".join(res)