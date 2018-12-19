# Runtime: 68 ms, faster than 7.48% of Python3 online submissions


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        rf_rc = 0
        rf_nc = nums[0]
        nf_rc = nums[1]
        nf_nc = 0
        for num in nums[2:-1]:
            rf_rc, rf_nc = rf_nc + num, max(rf_rc, rf_nc)
            nf_rc, nf_nc = nf_nc + num, max(nf_rc, nf_nc)
        return max(rf_rc, rf_nc, nf_rc, nf_nc + nums[-1])
