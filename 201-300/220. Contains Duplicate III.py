# Runtime: 48 ms, faster than 81.62% of Python3 online submissions


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or len(nums) <= 1 or t < 0:
            return False
        min_num, max_num = nums[0], nums[0]
        for num in nums[1:]:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
        buckets = {}
        for i in range(len(nums)):
            bi = (nums[i] - min_num) // (t + 1)
            if bi in buckets:
                return True
            if bi - 1 in buckets and nums[i] - buckets[bi - 1] <= t:
                return True
            if bi + 1 in buckets and buckets[bi + 1] - nums[i] <= t:
                return True
            if i >= k:
                buckets.pop((nums[i - k] - min_num) // (t + 1))
            buckets[bi] = nums[i]
        return False
