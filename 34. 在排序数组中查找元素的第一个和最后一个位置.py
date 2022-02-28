# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
# Constraints:
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non decreasing array.
# -10^9 <= target <= 10^9

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        if len(nums) == 0: return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                left, right = mid, mid
                while left > 0 and nums[left] == nums[left - 1]:
                    left -= 1
                while right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right += 1
                return [left, right]
            elif nums[mid] < target:
                while mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                    mid += 1
                left = mid + 1
            else:
                while mid > 1 and nums[mid] == nums[mid - 1]:
                    mid -= 1
                right = mid - 1

        return [-1, -1]


if __name__ == '__main__':
    a = [1,1,1,1,1,1,1]
    b = 1
    solution = Solution()
    c = solution.searchRange(a, b)
    print(c)