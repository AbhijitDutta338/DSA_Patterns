'''
Given the head of a sorted linked list, delete all duplicates 
such that each element appears only once. Return the linked list sorted as well.
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
    
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next   # remove duplicate
            else:
                curr = curr.next             # move only if no duplicate
        
        return head