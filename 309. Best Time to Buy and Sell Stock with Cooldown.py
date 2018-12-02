# Runtime: 56 ms, faster than 35.99% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
import sys


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        last_standby, standby = None, 0
        last_holding, holding = None, -sys.maxsize - 1
        last_cooling, cooling = None, -sys.maxsize - 1

        for price in prices:
            last_standby = standby
            last_holding = holding
            last_cooling = cooling

            standby = max(last_standby, last_cooling)
            holding = max(last_standby - price, last_holding)
            cooling = last_holding + price

        return max(standby, cooling)
