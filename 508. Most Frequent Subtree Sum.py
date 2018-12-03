# Runtime: 72 ms, faster than 51.92% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rec = {}

        def calsum(node):
            if not node:
                return 0
            subsum = node.val + calsum(node.left) + calsum(node.right)
            if subsum in rec:
                rec[subsum] += 1
            else:
                rec.setdefault(subsum, 1)
            return subsum

        calsum(root)
        maxsum = max(rec.values())
        res = []
        for k in rec:
            if rec[k] == maxsum:
                res.append(k)
        return res
