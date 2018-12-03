# Runtime: 44 ms, faster than 99.78% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        now = root
        last = TreeNode(None)
        rights = []

        while now or rights:
            if now:
                last.right = now
                last.left = None
                last = last.right
                rights.append(now.right)
                now = now.left
            else:
                now = rights.pop()
