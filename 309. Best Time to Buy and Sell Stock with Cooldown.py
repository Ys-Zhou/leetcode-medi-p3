# Runtime: 56 ms, faster than 35.99% of Python3 online submissions


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        last_standby, standby = None, 0
        last_holding, holding = None, -9223372036854775808
        last_cooling, cooling = None, -9223372036854775808

        for price in prices:
            last_standby = standby
            last_holding = holding
            last_cooling = cooling

            standby = max(last_standby, last_cooling)
            holding = max(last_standby - price, last_holding)
            cooling = last_holding + price

        return max(standby, cooling)
