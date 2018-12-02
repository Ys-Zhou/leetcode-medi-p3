# Runtime: 240 ms, faster than 31.66% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def tree(p_root, i_start, i_end):
            if i_end == i_start:
                return None
            i_root = inorder.index(postorder[p_root])
            root = TreeNode(postorder[p_root])
            root.right = tree(p_root - 1, i_root + 1, i_end)
            root.left = tree(p_root - i_end + i_root, i_start, i_root)
            return root

        return tree(len(postorder) - 1, 0, len(inorder))
