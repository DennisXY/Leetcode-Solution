# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one.
#
# You are given an API bool isBadVersion(version) which will return whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.
#
# Example:
#
# Given n = 5, and version = 4 is the first bad version.
#
# call isBadVersion(3) -> false
# call isBadVersion(5)-> true
# call isBadVersion(4)-> true
#
# Then 4 is the first bad version.

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left <= right:
            midpoint = (left+right) // 2
            if not isBadVersion(midpoint):
                left = midpoint + 1
            else:
                right = midpoint - 1
        return left