# Runtime: 5492 ms, faster than 40.94% of Python3 online submissions


class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        rec = [[0] * len(B) for _ in A]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i != 0 and j != 0:
                        rec[i][j] = rec[i - 1][j - 1] + 1
                    else:
                        rec[i][j] = 1
        return max([max(x) for x in rec])
