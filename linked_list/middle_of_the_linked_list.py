# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        m = 0
        fir = head
        while (head != None):
            head = head.next
            n += 1
        
        while (fir):
            m += 1
            if m == (n//2)+1:
                return (fir)
            else:
                fir = fir.next
        
