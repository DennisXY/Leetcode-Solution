# 输入一个字符串，打印出该字符串中字符的所有排列。
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]

class Solution:
    def permutation(self, s: str) -> List[str]:
        def backtrack(first):
            if first == n-1:
                temp = "".join(s)
                res.append(temp)
                return
            check = list()
            for i in range(first, n):
                if s[i] in check: continue
                check.append(s[i])
                s[first], s[i] = s[i], s[first]
                backtrack(first+1)
                s[first], s[i] = s[i], s[first]

        res = list()
        n = len(s)
        s = list(s)
        backtrack(0)
        return res