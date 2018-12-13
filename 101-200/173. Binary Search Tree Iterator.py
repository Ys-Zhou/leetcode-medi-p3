# No Python3 interpreter
# Runtime: 52 ms, faster than 92.22% of Python online submissions

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        node = root
        self.stack = []
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        next_node = node.right
        while next_node:
            self.stack.append(next_node)
            next_node = next_node.left
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
