# Runtime: 128 ms, faster than 32.83% of Python3 online submissions


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        pro = 1
        for i in range(len(nums)):
            res.append(pro)
            pro *= nums[i]
        pro = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pro
            pro *= nums[i]
        return res
