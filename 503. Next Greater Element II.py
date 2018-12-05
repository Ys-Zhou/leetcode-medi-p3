# Runtime: 176 ms, faster than 85.13% of Python3 online submissions


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []  # [num,index]
        for i in range(len(nums)):
            while stack and stack[-1][0] < nums[i]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
            stack.append((nums[i], i))
        for i in range(len(nums)):
            if not stack or stack[-1][1] == i:
                break
            while stack and stack[-1][0] < nums[i]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
        return res
