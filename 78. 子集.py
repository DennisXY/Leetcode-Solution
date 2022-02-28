# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution:
    def subsets(self, nums) -> List[List[int]]:
        result = list()
        result.append(list())

        for i in nums:
            result += [j + [i] for j in result]
        return result