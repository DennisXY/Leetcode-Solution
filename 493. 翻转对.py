# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
# You need to return the number of important reverse pairs in the given array.

# Example1:
# Input: [1,3,2,3,1]
# Output: 2

# Example2:
# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.

# 不能遍历数组，O(n^2),超时
# 分治算法，子问题A1的答案 + 子问题A2的答案 + 跨越A1和A2的答案，套娃
# 跨越A1/A2时，如果是两个数组是有序的，就可以不用遍历
# 步骤：
# 初始化两个指针i，j分别指向A1，A2的头部
# 如果A1[i] > 2*A2[j],那么A1[i]及A1[i]后面的所有元素都符合要求，更新答案并后移j
# 否则，后移i
# 接下来我们需要合并A1，A2以备解决后面更大的子问题使用
# 返回我们的答案
class Solution:

    #A1和A2之间
    def find_reversed_pairs(self ,nums ,left ,right):
        res ,mid = 0 ,(left+right )//2

        j = mid +1
        for i in range(left ,mid +1):
            while j <= right and nums[i] > 2* nums[j]:
                res += mid - i + 1
                j += 1
        return res

    def merge_sort(self, nums, nums_sorted, l, r):
        if l >= r: return 0
        mid = (l + r) // 2
        res = self.merge_sort(nums, nums_sorted, l, mid) + \
              self.merge_sort(nums, nums_sorted, mid + 1, r) + \
              self.find_reversed_pairs(nums, l, r)

        # Fill in the sort_num
        i, j, k = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                nums_sorted[k] = nums[i]
                i += 1
            else:
                nums_sorted[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            nums_sorted[k] = nums[i]
            i += 1
            k += 1
        while j <= r:
            nums_sorted[k] = nums[j]
            j += 1
            k += 1

        for k in range(l, r + 1): nums[k] = nums_sorted[k]

        return res

    def reversePairs(self, nums):
        if not nums: return 0
        #已经排序过的
        nums_sorted = [0] * len(nums)
        return self.merge_sort(nums, nums_sorted, 0, len(nums) - 1)


if __name__ == '__main__':
    a = [-5, -5]
    solution = Solution()
    b = solution.reversePairs(a)
    print(b)