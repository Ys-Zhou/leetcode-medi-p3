# Runtime: 48 ms, faster than 76.11% of Python3 online submissions
# Memory Usage: 15.7 MB, less than 5.93% of Python3 online submissions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        op, ep, eh = head, head.next, head.next
        while True:
            if ep.next:
                op.next = ep.next
                op = op.next
            else:
                break
            if op.next:
                ep.next = op.next
                ep = ep.next
            else:
                ep.next = None
                break
        op.next = eh
        return head
