# Runtime: 468 ms, faster than 62.83% of Python3 online submissions


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wordList = set(wordList)
        last_words = {beginWord}
        layer = 1
        while last_words:
            now_words = set()
            layer += 1
            for word in last_words:
                for i in range(len(word)):
                    word_li = list(word)
                    for j in range(97, 123):
                        word_li[i] = chr(j)
                        new_word = ''.join(word_li)
                        if new_word in wordList:
                            if new_word == endWord:
                                return layer
                            now_words.add(new_word)
                            wordList.remove(new_word)
            last_words = now_words
        return 0
