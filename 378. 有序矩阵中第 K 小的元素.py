# 给你一个 n x n 矩阵matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
# 输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# 输出：13
# 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13

# 二分法
# 矩阵中大于mid的数就和不大于mid的数分别形成了两个板块，沿着一条锯齿线将这个矩形分开。
# 其中左上角板块的大小即为矩阵中不大于mid的数的数量。


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        m, n = len(matrix), len(matrix[0])
        while l != r:
            mid = (l + r) // 2
            left = 0
            for i in range(n):
                if matrix[-1][i] <= mid:
                    left += n
                    continue
                for j in range(m - 1, -1, -1):
                    if matrix[j][i] > mid:
                        continue
                    else:
                        left += j + 1
                        break
            if left >= k:
                r = mid
            else:
                l = mid + 1
        return l

