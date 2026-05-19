class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str,  board: List[List[str]], visited: List[List[bool]], rows: int, cols: int, r: int, c: int) -> bool:
        node = self
        def dfs(r, c, idx):
            if idx == len(word):
                return node.is_end_of_word
            elif 0<=r<rows and 0<=c<cols and not visted[r][c]:
                char = board[r][c]
                visited[r][c] = True   # mark as visited
                if char not in node.children[char]:
                    return False
                node = node.children[char]

                return dfs(r + 1, c, idx) or dfs(r - 1, c, idx) or dfs(r, c + 1, idx) or dfs(r, c - 1, idx)
            else:
                return False
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        Trie = TrieNode()
        catcher = dict()

        for word in words:
            catcher[word[0]] = word
            Trie.insert(word)
        
        rows = len(board)
        cols = len(board[0])
        result = []
        visited = [[False]*rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in catcher and Trie.search(word, board, visited, rows, cols, r, c):
                    result.append(word)
        
        return result
                    

    