# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, None, None)

    def validate(self, node: Optional[TreeNode], minVal: Optional[int], maxVal: Optional[int]) -> bool:
        if node is None:
            return True

        if minVal is not None and node.val <= minVal:
            return False

        if maxVal is not None and node.val >= maxVal:
            return False

        return (
            self.validate(node.left, minVal, node.val) and
            self.validate(node.right, node.val, maxVal)
        )
'''
minAllowed < node.val < maxAllowed
Each subtree must know:
    the minimum allowed value
    the maximum allowed value
Without that, nodes can violate ancestors silently.
'''