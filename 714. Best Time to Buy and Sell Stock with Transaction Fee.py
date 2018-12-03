# Runtime: 128 ms, faster than 98.05% of Python3 online submissions


class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        minp = 50000
        maxp = 50000
        prof = 0
        for price in prices:
            if maxp - minp > fee:
                if price > maxp:
                    maxp = price
                elif price < maxp - fee:
                    prof += maxp - minp - fee
                    minp = maxp = price
            else:
                if price > maxp:
                    maxp = price
                elif price < minp:
                    minp = maxp = price
        prof += max(0, maxp - minp - fee)
        return prof
