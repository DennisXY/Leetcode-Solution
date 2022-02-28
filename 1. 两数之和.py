# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    def twoSum(self, nums, target):

        hash_map = {};
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hash_map:
                return[hash_map[another_num], index]
            hash_map[num] = index
        return None

if __name__ == '__main__':
    a = input("Please input the list: ").split(' ')
    a = list(a)
    solution = Solution()
    b = solution.findRepeatNumber(a)
    print(b)


#Using dictonary.