# Runtime: 56 ms, faster than 97.44% of Python3 online submissions
# Memory Usage: 14.6 MB, less than 5.26% of Python3 online submissions


class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        smallest_single = 9999999999
        smallest_double = 9999999999
        for num in nums:
            if num > smallest_double:
                return True
            if smallest_double > num > smallest_single:
                smallest_double = num
            elif smallest_single > num:
                smallest_single = num
        return False
