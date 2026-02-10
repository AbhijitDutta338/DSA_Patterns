#BFS Code

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list:
        if root is None:
            return []

        result = []
        queue = deque()
        queue.append(root)

        #BFS traversal, we process nodes level by level
        while queue:
            levelSize = len(queue) #Number of nodes at the current level
            level = []

            for _ in range(levelSize):
                node = queue.popleft()
                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level)
        return result