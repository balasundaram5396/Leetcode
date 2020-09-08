# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return 0
        start,end=head,head.next
        while end and end.next:
            if start==end:
                return True
            start=start.next
            end=end.next.next
        return False
        
        
            
        