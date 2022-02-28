#Given n non-negative integers representing the histogram's bar height
# where the width of each bar is 1, find the area of largest rectangle in the histogram.
#Solution:
#https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/

#From left 2 right and right 2 left
#left []: find the column left to the current which are shorter, if not, set to -1 as the sentry
class Solution:
    def largestRectangleArea(self, heights):
        length = len(heights)
        if length == 0: return 0
        left, right = [0]*length, [0]*length
        mono_stack = list()

        for i in range(length):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(length-1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else length
            mono_stack.append(i)
        result = max((right[i]-left[i]-1)*heights[i] for i in range(length))
        return result