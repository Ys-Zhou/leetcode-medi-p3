# Runtime: 84 ms, faster than 98.97% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        current_idx = 1

        def dfs(node):
            if not node:
                return None
            res = dfs(node.left)
            if res is not None:
                return res
            nonlocal current_idx
            if current_idx == k:
                return node.val
            current_idx += 1
            res = dfs(node.right)
            if res is not None:
                return res
            return None

        return dfs(root)
