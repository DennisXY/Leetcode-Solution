# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

class Solution:

    def sortColors(self, nums):
        start = 0
        end = len(nums) - 1
        current = 0
        while current <= end:
            if nums[current] == 0:
                nums[start], nums[current] = nums[current], nums[start]
                start += 1
                current += 1
            elif nums[current] == 2:
                nums[end], nums[current] = nums[current], nums[end]
                end -= 1
            else:
                current += 1

if __name__ == '__main__':

    a = [2, 0, 1]
    solution = Solution()
    solution.sortColors(a)
    print(a)