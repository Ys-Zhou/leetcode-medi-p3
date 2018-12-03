# Runtime: 868 ms, faster than 62.56% of Python3 online submissions


class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        p = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for x in range(len(s1)):
            p[x + 1][0] = p[x][0] + ord(s1[x])
        for y in range(len(s2)):
            p[0][y + 1] = p[0][y] + ord(s2[y])
        for x in range(len(s1)):
            for y in range(len(s2)):
                if s1[x] == s2[y]:
                    p[x + 1][y + 1] = p[x][y]
                else:
                    p[x + 1][y + 1] = min(p[x + 1][y] + ord(s2[y]), p[x][y + 1] + ord(s1[x]))
        return p[len(s1)][len(s2)]
