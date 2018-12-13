# Runtime: 44 ms, faster than 74.69% of Python3 online submissions


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        bp = [0]
        for end in range(len(s)):
            for start in bp:
                if s[start:end + 1] in wordDict:
                    if end == len(s) - 1:
                        return True
                    bp.append(end + 1)
                    break
        return False
