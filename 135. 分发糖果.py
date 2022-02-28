# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Example 1:
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        left = [0] * length
        result = 0

        for i in range(length):
            if i > 0 and ratings[i - 1] < ratings[i]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        right = 0
        for i in range(length - 1, -1, -1):
            if i < length - 1 and ratings[i + 1] < ratings[i]:
                right += 1
                result += max(left[i], right)
            else:
                right = 1
                result += left[i]

        return result

