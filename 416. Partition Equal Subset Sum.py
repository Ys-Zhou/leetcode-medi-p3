# Runtime: 52 ms, faster than 81.40% of Python3 online submissions


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums, reverse=True)
        sum_ = sum(nums)
        half = sum_ / 2

        if sum_ % 2 == 1:
            return False

        def select(total, rest, idx):
            if total == half:
                return True
            if total > half or total + rest < half:
                return False
            if idx == len(nums):
                return False
            return select(total + nums[idx], rest - nums[idx], idx + 1) or select(total, rest - nums[idx], idx + 1)

        return select(0, sum_, 0)
