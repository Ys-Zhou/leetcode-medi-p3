# Runtime: 56 ms, faster than 98.67% of Python3 online submissions
import collections


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = list(collections.Counter(tasks).values())
        maxtask = max(task_count)
        last = task_count.count(maxtask)
        return max(len(tasks), (maxtask - 1) * (n + 1) + last)
