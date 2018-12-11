# No Python3 interpreter
# Runtime: 64 ms, faster than 18.13% of Python online submissions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
