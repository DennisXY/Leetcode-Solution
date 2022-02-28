# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#  
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums) -> int:
        result = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                temp = 1
                while current_num+1 in nums_set:
                    temp += 1
                    current_num += 1
                result = max(result, temp)
        return result