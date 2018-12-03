# Runtime: 1168 ms, faster than 2.83% of Python3 online submissions


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        stmt = [[0, []] for _ in range(numCourses)]
        for pair in prerequisites:
            stmt[pair[0]][1].append(pair[1])
            stmt[pair[1]][0] += 1

        pointer = 0
        while 0 <= pointer < len(stmt):
            if stmt[pointer] and stmt[pointer][0] == 0:
                for d in stmt[pointer][1]:
                    stmt[d][0] -= 1
                stmt[pointer] = None
                pointer = 0
            else:
                pointer += 1

        return not any(stmt)
