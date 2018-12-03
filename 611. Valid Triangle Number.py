# Runtime: 232 ms, faster than 71.53% of Python3 online submissions

class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 3:
            return 0
        count = 0
        nums.sort()
        for c in range(length - 1, 1, -1):
            a = 0
            b = c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    count += b - a
                    b -= 1
                else:
                    a += 1
        return count
