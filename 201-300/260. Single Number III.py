# Runtime: 56 ms, faster than 34.69% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        x = 0
        for n in nums:
            x ^= n
        x &= -x
        a, b = 0, 0
        for n in nums:
            if n & x:
                a ^= n
            else:
                b ^= n
        return [a, b]
