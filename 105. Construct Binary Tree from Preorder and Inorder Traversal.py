# Runtime: 112 ms, faster than 86.24% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def c_tree(idx, start, end):
            if start == end:
                return None
            root = TreeNode(preorder[idx])
            root_idx = inorder.index(preorder[idx])
            root.left = c_tree(idx + 1, start, root_idx)
            root.right = c_tree(idx + 1 + root_idx - start, root_idx + 1, end)
            return root

        return c_tree(0, 0, len(preorder))
