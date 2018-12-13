# Runtime: 72 ms, faster than 19.87% of Python3 online submissions


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = -float('inf')
        dp = [[1, 1]]
        for i in range(len(nums)):
            dp.append([max(dp[i][0] * nums[i], dp[i][1] * nums[i], nums[i]),
                       min(dp[i][0] * nums[i], dp[i][1] * nums[i], nums[i])])
            max_ = max(max_, dp[-1][0])
        return max_
