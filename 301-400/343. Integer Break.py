# Runtime: 40 ms, faster than 57.58% of Python3 online submissions
# Memory Usage: 13.6 MB, less than 11.11% of Python3 online submissions


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return 3 ** (n // 3)
        if n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        return 3 ** (n // 3) * 2
