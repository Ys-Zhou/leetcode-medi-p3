# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def quick_sort(start, stop):
            if start.next == stop:
                return
            global new_head
            new_head = start
            select = last = start
            compare = select.next
            while compare != stop:
                if compare.val < select.val:
                    last.next = compare.next
                    compare.next = new_head
                    new_head = compare
                    compare = last.next
                else:
                    last = compare
                    compare = compare.next
            quick_sort(select, compare)
            quick_sort(new_head, select)

        quick_sort(head, None)
        return new_head


sol = Solution()
h = ListNode(-1)
h.next = ListNode(5)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
sol.sortList(h)
