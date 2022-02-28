# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Return 0 if the array contains less than 2 elements.
#
# Example 1:
#
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
#             (3,6) or (6,9) has the maximum difference 3.
# Example 2:
#
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
# Note:
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
# Try to solve it in linear time/space.

#桶排序
#相邻字的最大间距不会小于[(max-min)/(N-1)] (反证法)
#元素之间的最大间距一定不会出现在某个桶的内部，而一定会出现在不同桶当中。

class Solution:
    def maximumGap(self, nums):
        if not nums or len(nums) < 2: return 0

        Min = min(nums)
        Max = max(nums)
        bucket_size = max(1, (Max - Min)//(len(nums)-1))
        max_gap = 0
        buckets = [[] for i in range((Max - Min) // bucket_size + 1)]

        for num in nums:
            loc = (num - Min) // bucket_size
            buckets[loc].append(num)

        prev_max = float('inf')
        for bucket in buckets:
            if bucket and prev_max != float('inf'):
                max_gap = max(max_gap, min(bucket)-prev_max)
            if bucket:
                prev_max = max(bucket)
        return max_gap


