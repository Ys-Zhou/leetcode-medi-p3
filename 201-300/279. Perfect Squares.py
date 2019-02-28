# Runtime: 9860 ms, faster than 5.05% of Python3 online submissions
# Memory Usage: 13.3 MB, less than 36.50% of Python3 online submissions


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1, n + 1):
            num = 1 + dp[-1]
            s = 2
            while i >= s ** 2:
                num = min(num, 1 + dp[i - s ** 2])
                s += 1
            dp.append(num)
        return dp[-1]
