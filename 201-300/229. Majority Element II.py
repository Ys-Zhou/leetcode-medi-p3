# Runtime: 44 ms, faster than 100.00% of Python3 online submissions


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        num_1, num_2 = nums[0], nums[0]
        votes_1, votes_2 = 0, 0
        for num in nums:
            if num == num_1:
                votes_1 += 1
                continue
            if num == num_2:
                votes_2 += 1
                continue
            if votes_1 == 0:
                num_1 = num
                votes_1 = 1
                continue
            if votes_2 == 0:
                num_2 = num
                votes_2 = 1
                continue
            votes_1 -= 1
            votes_2 -= 1
        votes_1, votes_2 = 0, 0
        for num in nums:
            if num == num_1:
                votes_1 += 1
                continue
            if num == num_2:
                votes_2 += 1
                continue
        res = []
        if votes_1 > len(nums) // 3:
            res.append(num_1)
        if votes_2 > len(nums) // 3:
            res.append(num_2)
        return res
