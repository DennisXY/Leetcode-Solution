# A sequence of numbers is called arithmetic if it consists of at least three elements and
# if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequences:
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic.
#
# 1, 1, 2, 5, 7
# A zero-indexed array A consisting of N numbers is given.
# A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of the array A is called arithmetic if the sequence:
# A[P], A[P+ 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A.
#
# Example:
#
# A = [1, 2, 3, 4]
#
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

class Solution:
    def numberOfArithmeticSlices(self, A):

        # Calculate how many subsets.
        def calculate(n):
            Sum = 0
            for i in range(3, n+1):
                Sum += i-3 + 1
            return Sum

        gap = []
        for i in range(1, len(A)):
            gap.append(A[i] - A[i-1])
        length = len(gap)
        start = 0
        end = 0
        result = 0
        while start < length - 1 and end < length - 1:
            if gap[end] == gap[end + 1]:
                end += 1
            else:
                if start == end:
                    start += 1
                    end += 1
                    continue
                else:
                    result += calculate(end - start + 2)
                    start = end
        if end - start + 1 == length:
            result = calculate(end - start + 2)
        elif end == length - 1 and start < end:
            result += calculate(end - start + 2)
        return result


if __name__ == '__main__':
    a = 1, 1, 2, 5, 7
    solution = Solution()
    c = solution.numberOfArithmeticSlices(a)
    print(c)

