# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head.next and n == 1:
            head = None
            return head

        current = head
        l = head
        i = 0
        while current:
            if i > n:
                l = l.next
            i += 1
            current = current.next

        if i == n:
            return head.next

        l.next = l.next.next

        return head