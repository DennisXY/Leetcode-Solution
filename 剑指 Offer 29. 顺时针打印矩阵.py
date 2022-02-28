# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

# 每次把数组做transpose
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return matrix
        def reverse_mat(mat):
            m, n = len(mat), len(mat[0])
            temp = list()
            for i in range(n-1, -1, -1):
                temp_row = list()
                for j in range(m):
                    temp_row.append(mat[j][i])
                temp.append(temp_row)
            return temp

        res = list()
        while len(matrix) > 1:
            for i in range(len(matrix[0])):
                res.append(matrix[0][i])
            matrix = reverse_mat(matrix[1:])
        for i in range(len(matrix[0])):
            res.append(matrix[0][i])
        return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return matrix
        if len(matrix) <= 1:
            if matrix[0]:
                return matrix[0]
            else:
                return matrix
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result = list()
        if left == right:
            for i in range(down + 1):
                result.append(matrix[i][0])
            return result
        while left < right and up < down:
            for i in range(left, right + 1):
                result.append(matrix[up][i])
            up += 1
            for i in range(up, down + 1):
                result.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                result.append(matrix[down][i])
            down -= 1
            for i in range(down, up - 1, -1):
                result.append(matrix[i][left])
            left += 1
        if up == down:
            for i in range(left, right + 1):
                result.append(matrix[up][i])
        elif left == right:
            for i in range(up, down + 1):
                result.append(matrix[i][left])
        return result