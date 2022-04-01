# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
# and 128 % 8 == 0. A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing
# numbers in the range [left, right].


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = list()
        for i in range(left, right+1):
            temp = i
            while temp > 0:
                num = temp % 10
                if num == 0 or i % num != 0:
                    break
                else:
                    temp //= 10
            if temp == 0:
                result.append(i)
        return result