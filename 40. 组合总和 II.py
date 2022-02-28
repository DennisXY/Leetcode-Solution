# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates =[10,1,2,7,6,1,5], target =8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]


class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates: return []
        candidates.sort()  # 排序才能南蛮推进
        res = []

        def helper(i, nums, target):
            n = candidates[i]  # 这是base数
            if target < n:
                return  # 小于最小数，目标不能完成×
            if n == target:
                res.append(nums + [n]); return  # 目标能完成√
            if target == 0:
                res.append(nums); return  # 目标能完成√
            step = 1
            if i + step < len(candidates):
                helper(i + step, nums + [n], target - n)  # 先寻找选中base数的情况结果
            while i + step < len(candidates) and candidates[i + step] == n:
                step += 1  # 剪枝，略过相同base数的情况
            if i + step >= len(candidates):
                return  # 防止数组越界
            helper(i + step, nums, target)  # 不选择base数的其他情况

        helper(0, [], target)
        return res
