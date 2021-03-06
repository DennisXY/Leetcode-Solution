# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#             because they are adjacent houses.
# Example 2:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#            Total amount you can rob = 1 + 3 = 4.
class Solution:
    def rob(self, nums):
        temp_1 = 0 # without the last one
        temp_2 = 0 # without the first one
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])

        #Take the first house
        house = [0 for i in range(length)]
        house[0] = nums[0]
        house[1] = max(nums[0], nums[1])
        for i in range(2, length):
            house[i] = max(house[i-2]+nums[i], house[i-1])
        temp_1 = house[length - 2]

        #Take the second house
        house = [0 for i in range(length)]
        nums[0] = 0
        house[1] = max(nums[0], nums[1])
        for i in range(2, length):
            house[i] = max(house[i - 2] + nums[i], house[i - 1])
        temp_2 = house[length - 1]
        return max(temp_1, temp_2)
if __name__ == '__main__':
    a = [2,1,1,2]
    solution = Solution()
    c = solution.rob(a)
    print(c)