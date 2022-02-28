# Given two arrays arr1 and arr2, the elements of arr2 are distinct,
# and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
# Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

#
# Example 1:
#
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = [0] * 1001
        res = []
        # 统计arr1中每个数的频次
        for num in arr1:
            cnt[num] += 1

        # 按照arr2的顺序以及出现频次将每个数放入res中
        for num in arr2:
            res.extend([num] * cnt[num])
            cnt[num] = 0

        # 将桶中剩余元素按顺序和频次放入res数组后面
        for i in range(1001):
            if cnt[i] > 0:
                res.extend([i] * cnt[i])
        return res