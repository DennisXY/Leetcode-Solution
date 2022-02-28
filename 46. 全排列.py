# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# Same 剑指offer 38
class Solution:
    def permute(self, nums):
        def backtrack(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        res = list()
        n = len(nums)
        backtrack(0)
        return res

if __name__ == '__main__':

    a = [2, 0, 1]
    solution = Solution()
    solution.permute(a)
    print(a)