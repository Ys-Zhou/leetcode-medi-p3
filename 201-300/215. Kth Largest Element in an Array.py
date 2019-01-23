# Runtime: 1492 ms, faster than 14.63% of Python3 online submissions


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def half_quick_sort(start, end):
            if start == end:
                return nums[start]
            left, right = start, end
            while left < right:
                if nums[left] < nums[end]:
                    left += 1
                    continue
                if nums[right] >= nums[end]:
                    right -= 1
                    continue
                nums[left], nums[right] = nums[right], nums[left]
            nums[left], nums[end] = nums[end], nums[left]
            if left == len(nums) - k:
                return nums[left]
            if left < len(nums) - k:
                return half_quick_sort(left + 1, end)
            if left > len(nums) - k:
                return half_quick_sort(start, left - 1)

        return half_quick_sort(0, len(nums) - 1)
