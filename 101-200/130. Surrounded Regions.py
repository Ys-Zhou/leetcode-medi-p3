# Runtime: 208 ms, faster than 24.90% of Python3 online submissions


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        len_i = len(board)
        len_j = len(board[0])
        if len_i < 3 or len_j < 3:
            return
        for i in [0, -1]:
            for j in [0, -1]:
                if board[i][j] == 'O':
                    board[i][j] = 'R'

        def dfs(x, y):
            if x < 0 or x > len_i - 1 or y < 0 or y > len_j - 1:
                return
            if board[x][y] == 'O':
                board[x][y] = 'R'
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        for i in [0, len_i - 1]:
            for j in range(1, len_j - 1):
                dfs(i, j)
        for i in range(1, len_i - 1):
            for j in [0, len_j - 1]:
                dfs(i, j)
        for i in range(0, len_i):
            for j in range(0, len_j):
                if board[i][j] == 'R':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
