# Implement int sqrt(int x).
#
# Compute and return the square root of x
#

class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        start = 0
        end = x
        while True:
            mid = int((end + start) / 2)
            if mid ** 2 <= x and (mid+1) ** 2 > x:
                return mid
            if mid ** 2 > x:
                end = mid
                continue
            else:
                start = mid

if __name__ == '__main__':
    a = 2
    solution = Solution()
    x = solution.mySqrt(a)
    print(x)