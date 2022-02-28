# Given a string s, partition s such that
# every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
#
# A palindrome string is a string that reads the same backward as forward.
#
#
# Example 1:
#
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
#
# Input: s = "a"
# Output: [["a"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret