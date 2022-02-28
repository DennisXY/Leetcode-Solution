# Two strings X and Y are similar if we can swap two letters (in different positions) of X,
# so that it equals Y. Also two strings X and Y are similar if they are equal.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
# and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
# Notice that "tars" and "arts" are in the same group even though they are not similar.
# Formally, each group is such that a word is in the group if and only if
# it is similar to at least one other word in the group.
#
# We are given a list strs of strings where every string in strs
# is an anagram of every other string in strs. How many groups are there?
#
# Example 1:
#
# Input: strs = ["tars","rats","arts","star"]
# Output: 2
# Example 2:
#
# Input: strs = ["omv","ovm"]
# Output: 1

class DisjointSetUnion:
    def __init__(self, m, strs):
        self.parent = {}
        self.strs = strs
        self.cnt = m
        for i in range(m):
            self.parent[i] = i

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, x, y):
        num = 0
        for ac, bc in zip(x, y):
            if ac != bc:
                num += 1
                if num > 2:
                    return False
        return True

    def union(self, x, y):
        # if self.connected(self.strs[x], self.strs[y]): return
        parent_x = self.find(x)
        parent_y = self.find(y)
        self.parent[parent_x] = parent_y
        self.cnt -= 1


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        length = len(strs)
        group = DisjointSetUnion(length, strs)
        for i in range(length):
            for j in range(i + 1, length):
                fi, fj = group.find(i), group.find(j)
                if fi == fj:
                    continue
                if group.connected(strs[i], strs[j]):
                    # print(111)
                    group.union(i, j)

        result = 0
        for key, value in group.parent.items():
            if group.parent[key] == value:
                result += 1
        return group.cnt