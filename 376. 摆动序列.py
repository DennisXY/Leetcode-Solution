# A sequence of numbers is called a wiggle sequence
# if the differences between successive numbers strictly alternate between positive and negative.
# The first difference (if one exists) may be either positive or negative.
# A sequence with fewer than two elements is trivially a wiggle sequence.
#
# For example, [1,7,4,9,2,5] is a wiggle sequence
# because the differences (6,-3,5,-7,3) are alternately positive and negative.
# In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences,
# the first because its first two differences are positive and the second because its last difference is zero.
#
# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence.
# A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence,
# leaving the remaining elements in their original order.
#
# Example 1:
#
# Input: [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.
# Example 2:
#
# Input: [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
# Example 3:
#
# Input: [1,2,3,4,5,6,7,8,9]
# Output: 2
class Solution:
    def wiggleMaxLength(self, nums):
        length = len(nums)
        if length < 2:
            return length
        up = [1 for i in range (length)]
        down = [1 for i in range(length)]

        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[i - 1]:
                    up[i] = max(up[i], down[j] + 1)
                if nums[i] < nums[i - 1]:
                    down[i] = max(down[i], up[j] + 1)
        return max(max(down), max(up))

if __name__ == '__main__':
    a = [1,17,5,10,13,15,10,5,16,8]
    solution = Solution()
    c = solution.wiggleMaxLength(a)
    print(c)