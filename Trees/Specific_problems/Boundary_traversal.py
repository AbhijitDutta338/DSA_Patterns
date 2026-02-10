# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        #Adding the root to the result list as it is always part of the boundary    
        result = [root.val]

        #getting the leftBoundary and adding it to the result list, we start from root.left because root is already added
        self.addLeftBoundary(root.left, result)
        #getting leaf nodes for the left subtree
        self.addLeaves(root.left, result)
        #getting leaf nodes for the right subtree
        self.addLeaves(root.right, result)
        #getting the rightBoundary and adding it to the result list, we start from root.right because root is already added
        self.addRightBoundary(root.right, result)

        return result

    def addLeftBoundary(self, node: TreeNode, result: list) -> None:
        while node is not None:
            if not self.isLeaf(node):
                result.append(node.val)

            if node.left is not None:
                node = node.left
            else:
                node = node.right

    def addRightBoundary(self, node: TreeNode, result: list) -> None:
        stack = []

        while node is not None:
            if not self.isLeaf(node):
                stack.append(node.val)

            if node.right is not None:
                node = node.right
            else:
                node = node.left

        #Right boundary needs to be added in reverse order, 
        #so we pop from the stack and add to the result list
        while stack:
            result.append(stack.pop())

    def addLeaves(self, node: TreeNode, result: list) -> None:
        if node is None:
            return

        if self.isLeaf(node):
            result.append(node.val)
            return

        self.addLeaves(node.left, result)
        self.addLeaves(node.right, result)

    def isLeaf(self, node: TreeNode) -> bool:
        return node.left is None and node.right is None