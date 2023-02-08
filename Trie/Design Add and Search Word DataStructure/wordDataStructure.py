class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()         

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            # print(i, node.children.values())
            for j in range(i, len(word)):
                if word[j] == '.':
                    for child in node.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if word[j] not in node.children:
                        return False
                    node = node.children[word[j]]
            return node.endOfWord
        return dfs(0, self.root) 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
