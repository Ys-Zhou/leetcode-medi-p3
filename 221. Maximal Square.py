# Runtime: 136 ms, faster than 26.64% of Python3 online submissions


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        res_mat = [[0 for i in range(col)] for j in range(row)]
        now_max = 0
        for x in range(row):
            for y in range(col):
                if matrix[x][y] == '1':
                    if x == 0 or y == 0:
                        res_mat[x][y] = 1
                    else:
                        res_mat[x][y] = min(res_mat[x - 1][y - 1], res_mat[x - 1][y], res_mat[x][y - 1]) + 1
                    now_max = max(now_max, res_mat[x][y])
        return now_max ** 2
