# Runtime: 1120 ms, faster than 21.99% of Python3 online submissions
# Memory Usage: 17.2 MB, less than 38.91% of Python3 online submissions


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        idxs = [0] * len(primes)
        uglys = [1]
        for _ in range(n - 1):
            temp = []
            for i in range(len(primes)):
                while uglys[idxs[i]] * primes[i] <= uglys[-1]:
                    idxs[i] += 1
                temp.append(uglys[idxs[i]] * primes[i])
            uglys.append(min(temp))
        return uglys[-1]
