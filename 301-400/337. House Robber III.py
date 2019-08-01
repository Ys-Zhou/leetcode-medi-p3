# Runtime: 52 ms, faster than 93.49% of Python3 online submissions
# Memory Usage: 15.9 MB, less than 32.79% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            lv = dfs(node.left)
            rv = dfs(node.right)
            return node.val + lv[1] + rv[1], max(lv) + max(rv)

        return max(dfs(root))
