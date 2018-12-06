class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] <= nums[-1]:
            return nums[0]
        start = 0
        end = len(nums)
        idx = (start + end) // 2
        while nums[idx] > nums[idx - 1]:
            if nums[idx] > nums[0]:
                start = idx + 1
            else:
                end = idx
            idx = (start + end) // 2
        return nums[idx]
