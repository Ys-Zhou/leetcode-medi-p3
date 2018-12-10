# No Python3 interpreter
# Runtime: 68 ms, faster than 97.93% of Python online submissions

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        node = head
        while node:
            new_node = RandomListNode(node.label)
            new_node.next = node.next
            new_node.random = node.random
            node.next = new_node
            node = new_node.next
        node = head
        while node:
            if node.next.random:
                node.next.random = node.next.random.next
            node = node.next.next
        new_head = head.next
        node = head
        while node:
            new_node = node.next
            node.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            node = node.next
        return new_head
