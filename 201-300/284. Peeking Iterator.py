# Runtime: 52 ms, faster than 13.98% of Python3 online submissions
# Memory Usage: 13.3 MB, less than 5.77% of Python3 online submissions

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peeked = None
        self.it = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:
            self.peeked = self.it.next()
        return self.peeked

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            re = self.peeked
            self.peeked = None
            return re
        return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked:
            return True
        return self.it.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
