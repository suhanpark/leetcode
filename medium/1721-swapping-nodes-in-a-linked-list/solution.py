# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        l, r = None, head
        current = head
        n = 1

        while current:
            if n == k:
                l = current
            if n > k:
                r = r.next
            current = current.next
            n += 1
        
        l.val, r.val = r.val, l.val
        return head


