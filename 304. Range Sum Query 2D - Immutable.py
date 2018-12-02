# Runtime: 124 ms, faster than 20.62% of Python3 online submissions for Range Sum Query 2D - Immutable.


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                if x:
                    if y:
                        self.matrix[x][y] += self.matrix[x - 1][y] + self.matrix[x][y - 1] - self.matrix[x - 1][y - 1]
                    else:
                        self.matrix[x][y] += self.matrix[x - 1][y]
                else:
                    if y:
                        self.matrix[x][y] += self.matrix[x][y - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1:
            if col1:
                return self.matrix[row2][col2] - self.matrix[row2][col1 - 1] - self.matrix[row1 - 1][col2] + \
                       self.matrix[row1 - 1][col1 - 1]
            else:
                return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        else:
            if col1:
                return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
            else:
                return self.matrix[row2][col2]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
