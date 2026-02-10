'''
Why BST Makes LCA Easier

BST invariant:
    left subtree  <  node.val  <  right subtree
So at any node:
    If p.val < node.val and q.val < node.val
        → both nodes are in the left subtree
    If p.val > node.val and q.val > node.val
        → both nodes are in the right subtree
Otherwise
    → current node splits the paths → this is the LCA
No recursion needed to search both sides.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root

        while current is not None:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current

        return None