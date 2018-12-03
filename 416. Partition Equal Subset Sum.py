class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums, reverse=True)
        sum_ = sum(nums)
        if len(nums) == 1 or sum_ % 2 == 1:
            return False
        half = sum_ / 2
        psb = [0]
        for num in nums:
            next_psb = []
            sum_ -= num
            while (psb):
                p = psb.pop()


s = Solution()
s.canPartition([1, 5, 11, 5])
