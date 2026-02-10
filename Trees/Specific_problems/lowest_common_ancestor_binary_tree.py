'''
Given a binary tree (not necessarily a BST) and two nodes p and q, 
find their lowest common ancestor (LCA).

KeyIdea:
At any node, one of four situations is true:
    1. p is found in the left subtree
    2. q is found in the right subtree
    3. Both are found in the same subtree
    4. The current node is p or q
The LCA is the first node (lowest) where:
    1. one target is found on the left
    2. the other is found on the right
    OR
    the current node itself is p or q and the other is below it
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p, q)

    def find(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #None → neither p nor q exists in this subtree
        if node is None:
            return None

        #Node -> p or q → we found one of the targets, return it to the parent call 
        if node == p or node == q:
            return node

        #Check both subtrees for p & q
        leftResult = self.find(node.left, p, q)
        rightResult = self.find(node.right, p, q)

        #CASE: one target is found on the left and the other is found on the right
        #Because we are unwinding bottom-up: this is the LCA.
        if leftResult is not None and rightResult is not None:
            return node

        #Either one of p or q is in the left subtree, 
        #or LCA is already deeper in the left subtree, so we return whatever we got from the left subtree.
        if leftResult is not None:
            return leftResult

        #Symmetrically to return leftResult case, propagate upwards.
        return rightResult
