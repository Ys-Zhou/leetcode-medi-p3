# Runtime: 96 ms, faster than 97.80% of Python3 online submissions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        sp = head
        fp = head
        while fp.next:
            sp = sp.next
            fp = fp.next
            if fp.next:
                fp = fp.next
        mp = sp
        mq = mp.next
        mp.next = None
        while mq:
            mr = mq.next
            mq.next = mp
            mp = mq
            mq = mr
        np = head
        while fp is not sp:
            tnp = np.next
            tfp = fp.next
            np.next = fp
            fp.next = tnp
            np = tnp
            fp = tfp
