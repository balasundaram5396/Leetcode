# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        start,end=head,head
        st=[]
        
        while end and end.next:
            st.append(start.val)
            start=start.next
            end=end.next.next
        if end:
            start=start.next
        while start and len(st):
            if st.pop()!=start.val:
                return False
            start=start.next
        return True
            