# Runtime: 48 ms, faster than 99.45% of Python3 online submissions


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])

        def dig(sx, sy, ex, ey):
            if 0 <= sx < ex <= m and 0 <= sy < ey <= n:
                if ex - sx == 1:
                    start = sy
                    end = ey
                    while start < end:
                        mid = (start + end) // 2
                        if matrix[sx][mid] < target:
                            start = mid + 1
                        elif matrix[sx][mid] > target:
                            end = mid
                        elif matrix[sx][mid] == target:
                            return True
                elif ey - sy == 1:
                    start = sx
                    end = ex
                    while start < end:
                        mid = (start + end) // 2
                        if matrix[mid][sy] < target:
                            start = mid + 1
                        elif matrix[mid][sy] > target:
                            end = mid
                        elif matrix[mid][sy] == target:
                            return True
                else:
                    start = 0
                    end = min(ex - sx, ey - sy)
                    mid = -1
                    while mid != (start + end) // 2:
                        mid = (start + end) // 2
                        if matrix[sx + mid][sy + mid] < target:
                            start = mid
                        elif matrix[sx + mid][sy + mid] > target:
                            end = mid
                        elif matrix[sx + mid][sy + mid] == target:
                            return True
                    return dig(sx, sy + end, sx + end, ey) or dig(sx + end, sy, ex, sy + end)
            return False

        return dig(0, 0, m, n)
