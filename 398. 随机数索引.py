# Given an integer array nums with possible duplicates, randomly output the
# index of a given target number. You can assume that the given target number
# must exist in the array.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target.
# If there are multiple valid i's, then each index should have an
# equal probability of returning.
#  
#
# Example 1:
#
# Input
# ["Solution", "pick", "pick", "pick"]
# [[[1, 2, 3, 3, 3]], [3], [1], [3]]
# Output
# [null, 4, 0, 2]
#
# Explanation
# Solution solution = new Solution([1, 2, 3, 3, 3]);
# solution.pick(3); // It should return either index 2, 3, or 4 randomly.
# Each index should have equal probability of returning.
# solution.pick(1); // It should return 0. Since in the array only nums[0]
# is equal to 1.
# solution.pick(3); // It should return either index 2, 3, or 4 randomly.
# Each index should have equal probability of returning.

# 水塘抽样法：如何从未知或者很大样本N空间随机的取k个数
# 要保证每条数据被抽取到的概率相等，那么每个数被抽取的概率必然是k/N
# 前k个数全部保留，第i个数（i>k），以k/k概率保留，并以1/k的概率与前面k中任意一个替换


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1  # 第 cnt 次遇到 target
                if randrange(cnt) == 0:
                    ans = i
        return ans
