# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, balanced = self.check(root)
        return balanced

    def check(self, node: TreeNode) -> tuple:
        if node is None:
            return 0, True
        
        #Get the height and balance status of the left and right subtrees
        leftHeight, leftBalanced = self.check(node.left)
        rightHeight, rightBalanced = self.check(node.right)

        #Calculate current height
        currentHeight = max(leftHeight, rightHeight) + 1

        if not leftBalanced:
            return currentHeight, False

        if not rightBalanced:
            return currentHeight, False

        #Check if current node is balanced
        if abs(leftHeight - rightHeight) > 1:
            return currentHeight, False

        #If we reach here, it means the current node is balanced 
        #we can return the height and balance status
        return currentHeight, True