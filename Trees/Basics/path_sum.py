'''
Key Insight (the invariant)
At any node:
    “If I include this node in the path,
    how much sum is still required from my children?”
So we subtract current value and pass the remaining sum downward.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val

        #Check sum on leaf node
        if root.left is None and root.right is None:
            return targetSum == 0

        #Check if we can find the path sum in the left subtree, if we find it, 
        #we can return true immediately, otherwise we check the right subtree
        leftHasPath = self.hasPathSum(root.left, targetSum)
        if leftHasPath:
            return True

        #Check if we can find the path sum in the right subtree        
        return self.hasPathSum(root.right, targetSum)

