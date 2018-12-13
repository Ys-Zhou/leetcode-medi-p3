# Runtime: 36 ms, faster than 100.00% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def cal(total, node):
            nonlocal sum_
            total = total * 10 + node.val
            if not node.left and not node.right:
                sum_ += total
            else:
                if node.left:
                    cal(total, node.left)
                if node.right:
                    cal(total, node.right)

        if not root:
            return 0
        sum_ = 0
        cal(0, root)
        return sum_
