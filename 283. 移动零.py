# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left = right = 0

        while left < length and right < length:
            if nums[left] != 0:
                left += 1
                continue
            right = left + 1
            while right < length and nums[right] == 0:
                right += 1
            if right == length:
                return
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
