'''
Given the head of a singly linked list, group all the nodes with odd indices together 
followed by the nodes with even indices, and return the reordered list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        
        odd_head = head
        even_head = head.next
        
        odd, even = odd_head, even_head
        
        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        

        odd.next = even_head
        return odd_head