'''
Return the level-order traversal of a binary tree where:
Level 0 → left to right
Level 1 → right to left
Level 2 → left to right
… alternating each level

The only difference from normal level order is how you append values per level.
leftToRight (boolean) — flips after each level
'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = deque()
        queue.append(root)

        #Flag to determine the order of appending values for the current level
        leftToRight = True

        #BFS traversal, we process nodes level by level
        while queue:
            levelSize = len(queue)
            level = [0] * levelSize #Pre-allocate a list for the current level

            index = levelSize - 1
            if leftToRight:
                index = 0

            for _ in range(levelSize):
                node = queue.popleft()
                level[index] = node.val     #Append values in the correct order based on leftToRight flag

                if leftToRight:
                    index += 1
                else:
                    index -= 1

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level)
            leftToRight = not leftToRight

        return result