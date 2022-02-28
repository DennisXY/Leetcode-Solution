# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3

class NumArray:

    def __init__(self, nums):
        self.nums = nums
        length = len(nums)
        if length == 0:
            return None
        for i in range(1, length):
            nums[i] = nums[i] + nums[i-1]

    def sumRange(self, i, j):
        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i-1]

if __name__ == '__main__':
    a = [-2, 0, 3, -5, 2, -1]
    solution = NumArray(a)
    x = solution.sumRange(1, 1)
    print(x)