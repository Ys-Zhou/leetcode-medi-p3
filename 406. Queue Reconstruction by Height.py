# Runtime: 868 ms, faster than 4.23% of Python3 online submissions


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(people) - 1, -1, -1):
            for j in range(people[i][1]):
                people[i + j], people[i + j + 1] = people[i + j + 1], people[i + j]
        return people
