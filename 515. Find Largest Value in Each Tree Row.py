# Runtime: 228 ms, faster than 0.89% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        out = []
        max_val = root.val
        now_lvl = 0
        q = queue.Queue()
        q.put([root, 0])
        while not q.empty():
            node = q.get()
            if node[1] == now_lvl:
                max_val = max(max_val, node[0].val)
            else:
                out.append(max_val)
                max_val = node[0].val
                now_lvl = node[1]
            if node[0].left:
                q.put([node[0].left, now_lvl + 1])
            if node[0].right:
                q.put([node[0].right, now_lvl + 1])
        out.append(max_val)
        return out
