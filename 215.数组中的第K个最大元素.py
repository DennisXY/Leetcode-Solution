# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# Using quick sort
class Solution:
    def MySort(self , arr ):
        def quicksort(start, end):
            start_temp, end_temp = start, end
            pivot = end
            if start >= end:
                return
            while start < end:
                while arr[start] <= arr[pivot] and start < end:
                    start += 1
                while arr[end] >= arr[pivot] and start < end:
                    end -= 1
                if start < end:
                    arr[start], arr[end] = arr[end], arr[start]
            arr[end_temp], arr[start] = arr[start], arr[end_temp]
            quicksort(start_temp, start-1)
            quicksort(start+1, end_temp)
        quicksort(0, len(arr)-1)
        return arr

# Using heap sort
class Solution:
    def heapify(self, array, i, n):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and array[largest] < array[l]:
            largest = l
        if r < n and array[largest] < array[r]:
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]  # 交换
            self.heapify(array, largest, n)

    def findKthLargest(self, nums, k):
        n = len(nums)

        # 构建max_heap
        # 从叶子节点上面一层开始排，一直到root
        for i in range(int(n/2), -1, -1):
            self.heapify(nums, i, n)

        # 排列所有，因为只需要前k个排，不用排所有
        # for i in range(n - 1, 0, -1):
        #     nums[i], nums[0] = nums[0], nums[i]  # 交换
        #     self.heapify(nums, i, 0)

        for i in range(n-1, n-k-1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            n -= 1
            self.heapify(nums, 0, n)
        return nums[-k]


if __name__ == '__main__':
    a = [3,2,3,1,2,4,5,5,6]
    solution = Solution()
    b = solution.findKthLargest(a, 4)
    print(b)