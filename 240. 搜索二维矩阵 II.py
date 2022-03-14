# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix)-1, 0
        length = len(matrix[0])
        while m >= 0 and n < length:
            if matrix[m][n] == target:
                return True
            if matrix[m][n] > target:
                m -= 1
            else:
                n += 1
        return False