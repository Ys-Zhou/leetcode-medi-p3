# Runtime: 68 ms, faster than 8.77% of Python3 online submissions


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        rq = queue.Queue()
        lq = queue.Queue()
        rq.put(root)
        lq.put(0)
        while not rq.empty():
            node = rq.get()
            now_layer = lq.get()
            if node:
                if now_layer == len(res):
                    res.append(node.val)
                rq.put(node.right)
                lq.put(now_layer + 1)
                rq.put(node.left)
                lq.put(now_layer + 1)
        return res
