# Assume you are an awesome parent and want to give your children some cookies.
# You should give each child at most one cookie.
# Each child i has agreed factor gi,
# which is the minimum size of a cookie that the child will be content with;
# each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
# and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
#
# Example 1:
# Input: [1,2,3], [1,1]
#
# Output: 1
#
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1,
# you could only make the child whose greed factor is 1 content.
# You need to output 1.
# Example 2:
# Input: [1,2], [1,2,3]
#
# Output: 2
#
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the children,
# You need to output 2.

class Solution:
    def findContentChildren(self, g, s):
        #g:children, #s: biscuits
        g.sort()
        s.sort()
        cur_bis = 0
        cur_child = 0
        result = 0

        while cur_bis < len(s) and cur_child < len(g):
            if g[cur_child] <= s[cur_bis]:
                result += 1
                cur_child += 1
                cur_bis += 1
            else:
                cur_bis += 1
        return result

if __name__ == '__main__':
    a = [1,2]
    b = [1,2,3]
    solution = Solution()
    x = solution.findContentChildren(a, b)
    print(x)