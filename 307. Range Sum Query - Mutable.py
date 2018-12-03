# Runtime: 328 ms, faster than 22.65% of Python3 online submissions


class Node:

    def __init__(self):
        self.val = None
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            self.root = None
            return

        def make_tree(start, end):
            root = Node()
            if start == end:
                root.val = nums[start]
                return root
            left = make_tree(start, (start + end) // 2)
            right = make_tree((start + end) // 2 + 1, end)
            root.val = left.val + right.val
            root.left = left
            root.right = right
            return root

        self.nums = nums
        self.root = make_tree(0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        add = val - self.nums[i]
        self.nums[i] = val
        node = self.root
        start, end = 0, len(self.nums) - 1
        while node:
            node.val += add
            if i <= (start + end) // 2:
                node = node.left
                end = (start + end) // 2
            else:
                node = node.right
                start = (start + end) // 2 + 1

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        def cal_sum(node, start, end, x, y):
            if start == x and end == y:
                return node.val
            mid = (start + end) // 2
            if y <= mid:
                return cal_sum(node.left, start, mid, x, y)
            if x > mid:
                return cal_sum(node.right, mid + 1, end, x, y)
            if x <= mid < y:
                return cal_sum(node.left, start, mid, x, mid) + cal_sum(node.right, mid + 1, end, mid + 1, y)

        return cal_sum(self.root, 0, len(self.nums) - 1, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
