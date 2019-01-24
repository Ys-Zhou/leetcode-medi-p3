# Runtime: 2276 ms, faster than 0.97% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = None
        path_q = None

        def dfs(node, path):
            if not node:
                return
            nonlocal path_p, path_q
            if node.val == p.val:
                path_p = path.copy()
            elif node.val == q.val:
                path_q = path.copy()
            if path_p is not None and path_q is not None:
                return
            dfs(node.left, path + [0])
            dfs(node.right, path.copy() + [1])

        dfs(root, [])
        lca = root
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            if path_p[i] == 0:
                lca = lca.left
            else:
                lca = lca.right
            i += 1
        return lca
