# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next # 2 3 4 
            head.next = self.swapPairs(p.next) # 3, 4

            p.next = head # 2-> 1-> 
            return p 
        return head 

