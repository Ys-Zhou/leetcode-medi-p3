# Runtime: 628 ms, faster than 11.17% of Python3 online submissions


class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        mat = [set() for _ in range(n)]
        for pair in edges:
            mat[pair[0]].add(pair[1])
            mat[pair[1]].add(pair[0])

        nodes = set([x for x in range(n)])

        while (len(nodes) > 2):
            marked = set()
            for node in nodes:
                if len(mat[node]) == 1:
                    marked.add(node)
            for marked_node in marked:
                nodes.remove(marked_node)
                mat[mat[marked_node].pop()].remove(marked_node)
            nodes -= marked
        return list(nodes)
