# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        prev = None
        curr = head
        
        while curr:
            nextptr = curr.next
            curr.next = prev
            prev = curr
            curr = nextptr
            
        return prev
