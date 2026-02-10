# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        return 1 + min(leftDepth, rightDepth)


'''
minDepth(node) returns the length of the shortest root-to-leaf path starting at node
A missing child does not form a path.

Key Difference vs Max Depth (VERY important):
Min depth cannot pass through a null child.
Max depth can. -> Null children are harmless because we’re maximizing. 0 gets ignored.
Min depth cannot ignore null children because we’re minimizing. 0 would be the minimum 
if we ignore null children, but that’s not a valid path.
'''