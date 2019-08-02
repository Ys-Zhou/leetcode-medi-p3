# Runtime: 104 ms, faster than 47.11% of Python3 online submissions
# Memory Usage: 20 MB, less than 5.03% of Python3 online submissions


class Solution:
    def countBits(self, num: int) -> list:
        res = [0]
        pos = 1
        for i in range(1, num + 1):
            if i // pos == 1:
                res.append(1)
                pos *= 2
            else:
                res.append(1 + res[i % (pos // 2)])
        return res
