# Runtime: 32 ms, faster than 100.00% of Python3 online submissions


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        output = []
        start = 0
        first = 0
        last = len(nums)
        while start < len(nums):
            end = (first + last) // 2
            if end - start == nums[end] - nums[start]:
                if end == len(nums) - 1 or nums[end + 1] - nums[end] > 1:
                    if end == start:
                        output.append(str(nums[start]))
                    else:
                        output.append('%d->%d' % (nums[start], nums[end]))
                    start = end + 1
                    first = start
                    last = len(nums)
                else:
                    first = end + 1
            else:
                last = end
        return output
