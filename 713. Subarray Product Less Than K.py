# Runtime: 644 ms, faster than 20.90% of Python3 online submissions


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        first = 0
        last = 0
        prd = nums[0]
        res = 0
        while True:
            if prd < k:
                res += last - first + 1
                last += 1
                if last == len(nums):
                    break
                prd *= nums[last]
            else:
                if first < last:
                    prd /= nums[first]
                else:
                    last += 1
                    if last == len(nums):
                        break
                    prd = nums[last]
                first += 1
        return res
