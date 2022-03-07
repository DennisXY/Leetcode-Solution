# There are a total of numCourses courses you have to take,
# labeled from 0 to numCourses - 1. You are given an array prerequisites where
# prerequisites[i] = [ai, bi] indicates that you must take course bi first
# if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for i in edges[u]:
                if visited[i] == 1:
                    # 此时有环
                    valid = False
                    return
                elif visited[i] == 0:
                    dfs(i)
                    if not valid:
                        return
            visited[u] = 2

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        return valid