# Runtime: 244 ms, faster than 41.89% of Python3 online submissions
# Memory Usage: 13 MB, less than 5.26% of Python3 online submissions


class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        idx2, idx3, idx5 = 0, 0, 0
        ugly = [1]
        while len(ugly) < n:
            while ugly[idx2] * 2 <= ugly[-1]:
                idx2 += 1
            while ugly[idx3] * 3 <= ugly[-1]:
                idx3 += 1
            while ugly[idx5] * 5 <= ugly[-1]:
                idx5 += 1
            ugly.append(min(ugly[idx2] * 2, ugly[idx3] * 3, ugly[idx5] * 5))
        return ugly[-1]
