# Given an integer array nums and an integer k,
# return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# 建立一个小顶堆，然后遍历数组：
#
# 如果堆的元素个数小于 k，就可以直接插入堆中。
# 如果堆的元素个数等于 k，则检查堆顶与当前出现次数的大小。
# 如果堆顶更大，说明至少有 k 个数字的出现次数比当前值大，故舍弃当前值；
# 否则，就弹出堆顶，并将当前值插入堆中。
# 遍历完成后，堆中的元素就代表了「出现次数数组」中前 k 大的值。
# 复杂度 Nlogk


class Solution:
    def heapify(self, array, i, n):
        smallest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and array[smallest][1] > array[l][1]:
            smallest = l
        if r < n and array[smallest][1] > array[r][1]:
            smallest = r
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]  # 交换
            self.heapify(array, smallest, n)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        time = dict()
        for i in nums:
            if i not in time:
                time[i] = 1
            else:
                time[i] += 1

        time = list(time.items())
        heap = time[:k]

        for i in range(k):
            self.heapify(heap, i, k)

        for i in range(k, len(time)):
            if time[i][1] < heap[0][1]:
                continue
            heap[0] = time[i]
            for j in range(k):
                self.heapify(heap, j, k)

        result = list()
        for i in heap:
            result.append(i[0])
        return result