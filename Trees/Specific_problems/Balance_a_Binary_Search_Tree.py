# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []
        #sort the list using inoder traversal as its BST
        self.inorderTraversal(root, values)
        return self.buildBalancedBST(values, 0, len(values)-1)

    def inorderTraversal(self, node: TreeNode, values: list) -> None:
        if node is None:
            return
        self.inorderTraversal(node.left, values)
        values.append(node.val)
        self.inorderTraversal(node.right, values)

    def buildBalancedBST(self, values: list, left: int, right: int) -> TreeNode:
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(values[mid])

        root.left = self.buildBalancedBST(values, left, mid - 1)
        root.right = self.buildBalancedBST(values, mid + 1, right)

        return root