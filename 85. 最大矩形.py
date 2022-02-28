# Given a rows x cols binary matrix filled with 0's and 1's,
# find the largest rectangle containing only 1's and return its area.
# https://leetcode-cn.com/problems/maximal-rectangle/
# Solution:
# https://leetcode-cn.com/problems/maximal-rectangle/solution/python3-qian-zhui-he-dan-diao-zhan-ji-su-vkpp/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        pre = [0]*(m+1) #记录当前位置上方连续“1”的个数
        result = 0
        for i in range(n):
            for j in range(m):
                # 前缀和
                pre[j] = pre[j]+1 if matrix[i][j] == '1' else 0

            #单调栈
            stack = [-1]
            for k, num in enumerate(pre):
                while stack and pre[stack[-1]] > num:
                    index = stack.pop()
                    result = max(result, pre[index]*(k-stack[-1]-1))
                stack.append(k)

        return result