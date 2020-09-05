
# Given a linked list, remove the n-th node from the end of list and return its head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start=end=head
        for i in range(n):
            end=end.next
        if end is None:
            return head.next
        while end.next:
            end=end.next
            start=start.next
        start.next=start.next.next
        return head
        