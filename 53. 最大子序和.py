# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation:[4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums):

        pre = -100000
        maxAns = -100000
        for i in range(1, length):
            pre = max(pre+nums[i], nums[i])
            maxAns = max(pre, maxAns)

        return maxAns



if __name__ == '__main__':
    a =  [1, 2]
    solution = Solution()
    c = solution.maxSubArray(a)
    print(c)
