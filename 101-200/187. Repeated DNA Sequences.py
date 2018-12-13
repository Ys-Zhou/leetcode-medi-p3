# Runtime: 76 ms, faster than 92.24% of Python3 online submissions


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        int_map = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        char_map = [None, 'A', 'C', 'G', 'T']
        once = set()
        twice = set()
        now_char = 0
        for i in range(10):
            now_char = now_char * 10 + int_map[s[i]]
        once.add(now_char)
        for i in range(10, len(s)):
            now_char = (now_char % 1000000000) * 10 + int_map[s[i]]
            if now_char in twice:
                continue
            if now_char in once:
                once.remove(now_char)
                twice.add(now_char)
                continue
            once.add(now_char)
        res = []
        for num in twice:
            now_char = ''
            while num != 0:
                now_char = char_map[(num % 10)] + now_char
                num //= 10
            res.append(now_char)
        return res
