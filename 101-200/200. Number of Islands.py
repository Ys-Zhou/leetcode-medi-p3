# Runtime: 92 ms, faster than 48.40% of Python3 online submissions


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        def mark(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    mark(i - 1, j)
                    mark(i + 1, j)
                    mark(i, j - 1)
                    mark(i, j + 1)

        num = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    mark(x, y)
                    num += 1
        return num
