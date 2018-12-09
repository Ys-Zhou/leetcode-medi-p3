# No Python3 interpreter
# Runtime: 128 ms, faster than 3.57% of Python online submissions


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        most_left = None

        def do_conn(node):
            if not node:
                return
            if node.left and node.right:
                node.left.next = node.right
            nonlocal most_left  # Change this for Python2
            if node == most_left:
                most_left = None
            if node.right or node.left:
                if not most_left:
                    if node.left:
                        most_left = node.left
                    else:
                        most_left = node.right
                now_node = node
                while now_node.next:
                    now_node = now_node.next
                    if now_node.left:
                        if node.right:
                            node.right.next = now_node.left
                        else:
                            node.left.next = now_node.left
                        break
                    if now_node.right:
                        if node.right:
                            node.right.next = now_node.right
                        else:
                            node.left.next = now_node.right
                        break
            if node.next:
                do_conn(node.next)
            else:
                do_conn(most_left)

        do_conn(root)
