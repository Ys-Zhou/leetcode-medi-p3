# Runtime: 232 ms, faster than 1.04% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = queue.Queue()
        q.put(root)
        now = None
        while not q.empty():
            now = q.get()
            if now.right:
                q.put(now.right)
            if now.left:
                q.put(now.left)
        return now.val
