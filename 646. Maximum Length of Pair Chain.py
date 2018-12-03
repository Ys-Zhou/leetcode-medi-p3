# Runtime: 68 ms, faster than 94.42% of Python3 online submissions


class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        num = 0
        last = -9223372036854775808
        pairs.sort(key=lambda x: x[1])
        for pair in pairs:
            if pair[0] > last:
                num += 1
                last = pair[1]
        return num
