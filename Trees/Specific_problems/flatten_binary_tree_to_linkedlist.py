# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This is literally the same as pre-order traversal, we just need to connect the nodes as we go.
# We can use a stack to keep track of the nodes we need to visit. We push the right child first so that the left child is processed first.
# As we pop nodes from the stack, we connect them to the previous node in the linked list.

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        stack = []
        stack.append(root)
        prev = None #The headNode for the linked list

        while stack:
            current = stack.pop()

            # Connect the previous node to the current node
            if prev is not None:
                prev.left = None
                prev.right = current
            
            # Push right first so left is processed first
            if current.right is not None:
                stack.append(current.right)

            if current.left is not None:
                stack.append(current.left)
            
            # Update the previous node to the current node
            prev = current