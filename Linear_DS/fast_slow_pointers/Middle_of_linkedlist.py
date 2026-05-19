# LeetCode 876 - Middle of the Linked List (Fast and Slow Pointer Approach)
def middleNodeFastAndSlowPointerApproach(self, head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


#Brute Force Approach
def middleNodeCountingApproach(self, head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    current = head
    for _ in range(count // 2):
        current = current.next
    return current