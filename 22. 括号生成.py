# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]


class Solution:
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

if __name__ == '__main__':
    a = 2
    solution = Solution()
    c = solution.generateParenthesis(a)
    print(c)