# Runtime: 136 ms, faster than 20.19% of Python online submissions


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        le = len(s)
        dp = [[] for _ in range(le + 1)]
        dp[0].append([])
        for end in range(le):
            for start in range(end + 1):
                is_pal = True
                for p in range((end - start + 1) // 2):
                    if s[start + p] != s[end - p]:
                        is_pal = False
                        break
                if is_pal:
                    for div in dp[start]:
                        dp[end + 1].append(div + [s[start:end + 1]])
        return dp[-1]
