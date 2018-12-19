# Runtime: 264 ms, faster than 79.17% of Python3 online submissions


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.str_dict = dict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        now_dict = self.str_dict
        for char in word:
            if char not in now_dict:
                now_dict.setdefault(char, dict())
            now_dict = now_dict[char]
        now_dict.setdefault('#', None)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def search_char(idx, now_dict):
            if idx == len(word):
                if '#' in now_dict:
                    return True
                return False
            if word[idx] == '.':
                for char in now_dict:
                    if char != '#' and search_char(idx + 1, now_dict[char]):
                        return True
                return False
            else:
                if word[idx] in now_dict:
                    return search_char(idx + 1, now_dict[word[idx]])
                return False

        return search_char(0, self.str_dict)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
