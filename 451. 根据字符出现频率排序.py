# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.

class Solution(object):
    def frequencySort(self, s):

        def func(elem): # 自定义比较函数
            return elem[1]

        d = {}
        for c in s: # 记录词频
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        l = sorted(d.items(), key=func, reverse=True) # 根据词频进行排序
        res = []
        for i in l:
            res.append(i[0] * i[1]) # 根据词频生成相应数量的单词
        return "".join(res)

if __name__ == '__main__':

    # 遍历字典列表
    solution = Solution()
    # c = solution.frequencySort(a)
    # print(c)