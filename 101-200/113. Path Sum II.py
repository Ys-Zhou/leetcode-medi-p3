# Runtime: 72 ms, faster than 31.96% of Python3 online submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []

        if root:
            def cal(path: list, path_sum: int, node: TreeNode):
                now_path = path.copy()
                now_path.append(node.val)
                path_sum += node.val
                if not node.left and not node.right:
                    if path_sum == sum:
                        res.append(now_path)
                else:
                    if node.left:
                        cal(now_path, path_sum, node.left)
                    if node.right:
                        cal(now_path, path_sum, node.right)

            cal([], 0, root)
        return res
