# Runtime: 48 ms, faster than 43.36% of Python3 online submissions
# Memory Usage: 14.5 MB, less than 84.65% of Python3 online submissions


class Solution:
    def findDuplicate(self, nums: list) -> int:
        fast = nums[0]
        slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast
