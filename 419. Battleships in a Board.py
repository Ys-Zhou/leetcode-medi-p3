# Runtime: 72 ms, faster than 9.04% of Python3 online submissions


class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        count = 0
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'X' and (x == 0 or board[x - 1][y] == '.') and (y == 0 or board[x][y - 1] == '.'):
                    count += 1
        return count
