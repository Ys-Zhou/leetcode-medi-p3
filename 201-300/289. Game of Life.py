# Runtime: 32 ms, faster than 97.76% of Python3 online submissions
# Memory Usage: 13 MB, less than 89.74% of Python3 online submissions


class Solution:
    def gameOfLife(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        len_x = len(board)
        len_y = len(board[0])

        def live_neighbors(x: int, y: int) -> int:

            def convert(mark):
                if mark == 'D':
                    return 1
                if mark == 'L':
                    return 0
                return mark

            live_count = 0
            if x > 0:
                live_count += convert(board[x - 1][y])
                if x < len_x - 1:
                    live_count += convert(board[x + 1][y])
                    if y > 0:
                        live_count += convert(board[x - 1][y - 1]) + convert(board[x][y - 1]) + convert(
                            board[x + 1][y - 1])
                    if y < len_y - 1:
                        live_count += convert(board[x - 1][y + 1]) + convert(board[x][y + 1]) + convert(
                            board[x + 1][y + 1])
                else:  # x == len_x -1
                    if y > 0:
                        live_count += convert(board[x - 1][y - 1]) + convert(board[x][y - 1])
                    if y < len_y - 1:
                        live_count += convert(board[x - 1][y + 1]) + convert(board[x][y + 1])
            else:  # x == 0
                if x < len_x - 1:
                    live_count += convert(board[x + 1][y])
                    if y > 0:
                        live_count += convert(board[x][y - 1]) + convert(board[x + 1][y - 1])
                    if y < len_y - 1:
                        live_count += convert(board[x][y + 1]) + convert(board[x + 1][y + 1])
                else:  # x == len_x - 1
                    if y > 0:
                        live_count += convert(board[x][y - 1])
                    if y < len_y - 1:
                        live_count += convert(board[x][y + 1])
            return live_count

        for i in range(len_x):
            for j in range(len_y):
                if board[i][j] == 1:
                    lives = live_neighbors(i, j)
                    if lives < 2 or lives > 3:
                        board[i][j] = 'D'
                else:
                    if live_neighbors(i, j) == 3:
                        board[i][j] = 'L'

        for i in range(len_x):
            for j in range(len_y):
                if board[i][j] == 'D':
                    board[i][j] = 0
                elif board[i][j] == 'L':
                    board[i][j] = 1
