# Runtime: 392 ms, faster than 68.14% of Python3 online submissions
# Memory Usage: 13.3 MB, less than 79.95% of Python3 online submissions


class Solution:
    def maxProduct(self, words: list) -> int:
        mp = 0
        bins = []
        for word in words:
            b = 0
            for c in word:
                b |= 1 << ord(c) - ord('a')
            bins.append(b)
        for w1 in range(len(words)):
            for w2 in range(w1 + 1, len(words)):
                if bins[w1] & bins[w2] == 0:
                    mp = max(mp, len(words[w1]) * len(words[w2]))
        return mp
