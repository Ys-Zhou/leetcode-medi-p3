# Runtime: 40 ms, faster than 65.17% of Python3 online submissions


class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        extra = 0
        lowest = float('inf')
        lowest_p = 0
        for i in range(len(gas)):
            extra += gas[i] - cost[i]
            if gas[i] < cost[i] and extra < lowest:
                lowest = extra
                lowest_p = i
        if extra < 0:
            return -1
        return (lowest_p + 1) % len(gas)
