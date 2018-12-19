# Runtime: 352 ms, faster than 9.18% of Python3 online submissions


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [set() for _ in range(numCourses)]
        for edge in prerequisites:
            adj[edge[1]].add(edge[0])
        order = list()
        pre_num = list()

        def dfs(num):
            pre_num.append(num)
            for next_num in adj[num]:
                if next_num in pre_num:
                    raise Exception
                if next_num not in order:
                    dfs(next_num)
            order.append(num)
            pre_num.pop()

        try:
            for course in range(numCourses):
                if course not in order:
                    dfs(course)
        except Exception:
            return []
        order.reverse()
        return order
