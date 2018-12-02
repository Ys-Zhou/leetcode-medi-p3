# Runtime: 64 ms, faster than 16.34% of Python3 online submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = queue.Queue()
        nowlvl = 0
        q.put([root, 1])
        while not q.empty():
            node = q.get()
            if node[1] == nowlvl:
                res[-1].append(node[0].val)
            else:
                res.append([node[0].val])
                nowlvl = node[1]
            if node[0].left:
                q.put([node[0].left, node[1] + 1])
            if node[0].right:
                q.put([node[0].right, node[1] + 1])
        return res
