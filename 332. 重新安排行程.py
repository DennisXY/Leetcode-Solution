# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
# Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries,
# you should return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
import collections


class Solution:
    def findItinerary(self, tickets):
        d = collections.defaultdict(list)  # 邻接表
        for f, t in tickets:
            d[f] += [t]  # 路径存进邻接表

        for f in d:
            d[f].sort()  # 邻接表排序

        ans = []

        def dfs(f):  # 深搜函数
            while d[f]:
                dfs(d[f].pop(0))  # 路径检索
            ans.insert(0, f)  # 放在最前

        dfs('JFK')
        return ans

if __name__ == '__main__':
    a = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    solution = Solution()
    c = solution.findItinerary(a)
    #print(c)