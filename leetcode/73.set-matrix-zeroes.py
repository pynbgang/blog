#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:     #ping
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols, row0, col0 = len(matrix), len(matrix[0]), set(), set()
        for row in range(rows):             #scan whole matrix and look for
            for col in range(cols):         #the 0 elements, record it's
                if matrix[row][col] == 0:   #row/col number
                    col0.add(col)
                    row0.add(row)
        for i in row0:                      #fill zero for each row
            matrix[i] = [0] * cols
        for i in col0:                      #fill zero for each col
            for row in range(rows):
                matrix[row][i] = 0


class Solution:     #lmv
    def setZeroes(self, matrix):
        # First row has zero?
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n


# @lc code=end
