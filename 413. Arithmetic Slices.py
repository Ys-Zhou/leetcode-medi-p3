# Runtime: 36 ms, faster than 94.91% of Python3 online submissions


class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        sum_ = 0
        start = 0
        diff = A[1] - A[0]
        for end in range(2, len(A)):
            if A[end] - A[end - 1] != diff:
                sum_ += (end - start - 2) * (end - start - 1) // 2
                start = end - 1
                diff = A[end] - A[start]
        if len(A) - start >= 3:
            sum_ += (len(A) - start - 2) * (len(A) - start - 1) // 2
        return sum_
