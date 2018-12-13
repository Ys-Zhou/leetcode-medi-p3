# Runtime: 44 ms, faster than 38.32% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        rightstack = [root]
        leftstack = []

        while rightstack:
            layer = []
            while rightstack:
                if rightstack[-1] is not None:
                    layer.append(rightstack[-1].val)
                    leftstack.append(rightstack[-1].left)
                    leftstack.append(rightstack[-1].right)
                rightstack.pop()
            if layer:
                res.append(layer)
            layer = []
            while leftstack:
                if leftstack[-1] is not None:
                    layer.append(leftstack[-1].val)
                    rightstack.append(leftstack[-1].right)
                    rightstack.append(leftstack[-1].left)
                leftstack.pop()
            if layer:
                res.append(layer)
        return res
