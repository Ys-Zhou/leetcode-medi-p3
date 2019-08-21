# Runtime: 120 ms, faster than 63.15% of Python3 online submissions
# Memory Usage: 18.5 MB, less than 6.25% of Python3 online submissions


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        d = dict()
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d.setdefault(n, 1)
        return [item[0] for item in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]
