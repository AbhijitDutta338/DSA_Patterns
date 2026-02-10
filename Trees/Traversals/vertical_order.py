'''
This is BFS with coordinates.
Why BFS?
BFS naturally preserves top-to-bottom order
DFS can break ordering within the same column
Each node carries: (node, columnIndex)
'''

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        columnTable = {}
        queue = deque()
        queue.append((root, 0)) #Each node carries: (node, columnIndex)

        minCol = 0
        maxCol = 0

        #BFS traversal, we process nodes level by level
        while queue:
            node, col = queue.popleft()

            #Create column entry if it doesn't exist for current node
            if col not in columnTable:
                columnTable[col] = []
            
            #Append the current node's value to the list for its column
            columnTable[col].append(node.val)


            if node.left is not None:
                queue.append((node.left, col - 1))
                if col - 1 < minCol:
                    minCol = col - 1

            if node.right is not None:
                queue.append((node.right, col + 1))
                if col + 1 > maxCol:
                    maxCol = col + 1

        result = []
        #Add columns to the result list in order from minCol to maxCol
        for col in range(minCol, maxCol + 1):
            result.append(columnTable[col])

        return result