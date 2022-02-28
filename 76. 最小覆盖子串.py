# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in t
# (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.
#
#  
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
#https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/


import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        need_cnt = len(t)
        left = 0
        result = [0, float('inf')]
        for right, c in enumerate(s):
            if need[c] > 0:
                need_cnt -= 1
            need[c] -= 1
            if need_cnt == 0: # 滑动窗口包含所有t中元素
                while True: # 增加left，排除多余的元素
                    c = s[left]
                    if need[c] == 0:
                        break
                    need[c]+=1   # 如果有小于0的，代表多余了，继续走
                    left += 1
                if right-left < result[1]-result[0]:
                    result = [left, right]
                need[s[left]] += 1 # 增加left，寻找新的条件满足滑动窗口
                need_cnt += 1
                left += 1
        return '' if result[1] > len(s) else s[result[0]:result[1]+1]