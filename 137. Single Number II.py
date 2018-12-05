# Runtime: 40 ms, faster than 88.21% of Python3 online submissions


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b1 = 0
        b2 = 0
        for num in nums:
            b1 = b1 ^ num & ~b2
            b2 = b2 ^ num & ~b1
        return b1
