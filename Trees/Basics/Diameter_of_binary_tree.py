# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height, diameter = self.compute(root)
        return diameter

    def compute(self, node: TreeNode) -> tuple:
        if node is None:
            return 0, 0

        leftHeight, leftDiameter = self.compute(node.left)
        rightHeight, rightDiameter = self.compute(node.right)

        currentHeight = max(leftHeight, rightHeight) + 1
        currentDiameter = leftHeight + rightHeight

        bestDiameter = leftDiameter
        if rightDiameter > bestDiameter:
            bestDiameter = rightDiameter
        if currentDiameter > bestDiameter:
            bestDiameter = currentDiameter

        return currentHeight, bestDiameter