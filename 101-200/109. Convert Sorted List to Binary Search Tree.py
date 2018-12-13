# Runtime: 244 ms, faster than 12.45% of Python3 online submissions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        array = list()
        while head:
            array.append(head.val)
            head = head.next

        def create_tree(start, end):
            if start == end:
                return None
            root_idx = (start + end) // 2
            root = TreeNode(array[root_idx])
            root.left = create_tree(start, root_idx)
            root.right = create_tree(root_idx + 1, end)
            return root

        return create_tree(0, len(array))
