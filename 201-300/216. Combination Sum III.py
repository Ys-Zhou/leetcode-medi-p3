# Runtime: 56 ms, faster than 26.88% of Python3 online submissions


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums: list, num: int):
            if len(nums) == k:
                if sum(nums) == n:
                    res.append(nums)
                return
            if k - len(nums) > 10 - num:
                return
            dfs([] + nums + [num], num + 1)
            dfs([] + nums, num + 1)

        dfs([], 1)
        return res
