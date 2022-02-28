# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution:
    def findMin(self, nums) -> int:
        start = 0
        length = len(nums)
        end = len(nums) - 1
        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        while True:
            mid = int((start + end) / 2)
            if end - start + 1 == 2:
                return min(nums[start], nums[start+1])
            if end - start + 1 == 3:
                return min(nums[start], min(nums[start+1], nums[start+2]))
            if nums[start] > nums[mid]:
                end = mid
                continue
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

if __name__ == '__main__':
    a = [1,2,3,4,5]
    solution = Solution()
    c = solution.findMin(a)
    print(c)