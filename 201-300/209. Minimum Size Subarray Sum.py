# Runtime: 44 ms, faster than 99.59% of Python3 online submissions


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sum_ = 0
        min_len = len(nums) + 1
        start = 0
        for end in range(len(nums)):
            sum_ += nums[end]
            while sum_ >= s:
                min_len = min(min_len, end - start + 1)
                sum_ -= nums[start]
                start += 1
        if min_len == len(nums) + 1:
            return 0
        return min_len
