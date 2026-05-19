class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.is_end_of_word = True


    def search(self, word: str) -> bool:
        def dfs(node: WordDictionary, index: int) -> bool:
            if index == len(word):
                return node.is_end_of_word

            char = word[index]

            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
            
        return dfs(self, 0)

