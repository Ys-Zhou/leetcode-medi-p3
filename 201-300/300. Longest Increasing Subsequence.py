# Runtime: 28 ms, faster than 99.90% of Python3 online submissions
# Memory Usage: 13.2 MB, less than 63.33% of Python3 online submissions


class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        if not nums:
            return 0
        max_len = [-9223372036854775808]
        for n in nums:
            if n > max_len[-1]:
                max_len.append(n)
                continue
            for i in range(len(max_len) - 2, -1, -1):
                if n > max_len[i]:
                    max_len[i + 1] = n
                    break
        return len(max_len) - 1
