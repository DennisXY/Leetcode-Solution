# Given an integer array nums of length n where all the integers of nums are
# in the range [1, n] and each integer appears once or twice, return an array
# of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
#
#  
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# 根据正负号判断



class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
            else:
                ans.append(x)
        return ans
