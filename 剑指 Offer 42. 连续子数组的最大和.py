# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num_list = nums
        length=len(num_list)
        max_value=float('-inf')
        tmp=0
        left, right, temp = 0, 0, 0
        t= []
        for i in range(length):
            if tmp < 0:
                left = i
                right = 1
            else:
                right += 1
            tmp = max(tmp + num_list[i], num_list[i])
            max_value=max(max_value, tmp)
            if tmp == max_value:
                t.append((p, (p + q)))

        print(max_value,t[-1])
        return max_value