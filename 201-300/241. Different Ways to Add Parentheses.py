# Runtime: 36 ms, faster than 95.54% of Python3 online submissions


class Solution:
    def diffWaysToCompute(self, input: 'str') -> 'List[int]':
        nums = []
        opes = []
        cur_num = 0
        for char in input:
            if char == '+' or char == '-' or char == '*':
                nums.append(cur_num)
                cur_num = 0
                opes.append(char)
            else:
                cur_num = cur_num * 10 + int(char)
        nums.append(cur_num)

        def tree_search(si, ei):
            if ei - si == 1:
                return [nums[si]]
            res = []
            for bi in range(si + 1, ei):
                lr = tree_search(si, bi)
                rr = tree_search(bi, ei)
                if opes[bi - 1] == '+':
                    for ln in lr:
                        for rn in rr:
                            res.append(ln + rn)
                elif opes[bi - 1] == '-':
                    for ln in lr:
                        for rn in rr:
                            res.append(ln - rn)
                else:
                    for ln in lr:
                        for rn in rr:
                            res.append(ln * rn)
            return res

        return tree_search(0, len(nums))
