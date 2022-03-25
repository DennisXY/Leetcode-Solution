# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that
# do not appear in nums.
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
#
# 这题用鸽笼原理实现，由题意可得，1-n的位置表示1-n个笼子，如果出现过，
# 相应的“鸽笼”就会被占掉，我们将数字置为负数表示被占掉了。 最后再遍历一遍，
# 如果“鸽笼”为正数就是没出现的数字。


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for n in nums:
            nums[abs(n) - 1] = - 1
            # 找到相应的鸽笼位置，取反

        res = []
        for i, v in enumerate(nums):
            if v > 0:  # 如果大于0，说明没被占过，也就是没有出现过的数字
                res.append(i + 1)

        return res