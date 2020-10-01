# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA and headB is None:
            return
        ap=headA
        bp=headB

        while ap!=bp:
            ap=headB if ap==None else ap.next
            bp=headA if bp==None else bp.next
        return ap



#traverse through both LLs at a time,  if LL ends, point it to the head of the other LL
