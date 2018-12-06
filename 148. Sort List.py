# TLE

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def quick_sort(start, stop):
            if start.next == stop:
                return
            before = start
            after = before.next
            while after.next != stop:
                if before.next.val > after.next.val:
                    move = after.next
                    after.next = move.next
                    move.next = before.next
                    before.next = move
                    before = before.next
                else:
                    after = after.next
            quick_sort(start, before.next)
            quick_sort(before.next, stop)

        b_head = ListNode(None)
        b_head.next = head
        quick_sort(b_head, None)
        return b_head.next
