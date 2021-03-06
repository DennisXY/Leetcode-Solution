# You are given a sorted array consisting of only integers where
# every element appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.
#
# Follow up: Your solution should run in O(log n) time and O(1) space.

#
# Example 1:
#
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
#
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5

# 含有单个元素的子数组元素个数为奇数。
class Solution:
    def singleNonDuplicate(self, nums):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            halves_are_even = (hi - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halves_are_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves_are_even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]




if __name__ == '__main__':
    a = [1,1,2]
    solution = Solution()
    c = solution.singleNonDuplicate(a)
    print(c)