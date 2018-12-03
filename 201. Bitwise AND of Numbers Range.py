# Runtime: 420 ms, faster than 16.12% of Python3 online submissions


class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        i = 0
        while 1 << i <= n:
            if n - m < 1 << i and m & 1 << i and n & 1 << i:
                res |= 1 << i
            i += 1
        return res
