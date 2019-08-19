from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Solution:
    def __init__(self):
        self.result = set()

    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            curr = root
            for letter in word:
                curr = curr.children[letter]
            curr.word = word
        return root

    def findWords(self, board, words):
        root = self.buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(root, board, i, j)
        return list(self.result)

    def dfs(self, node, board, i,j):
        if node.word: self.result.add(node.word)
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            # Get character at board
            char = board[i][j]
            # If character is in it, then use the character for next loop
            child = node.children.get(char)
            if child:
                board[i][j] = None
                self.dfs(child, board, i + 1, j)
                self.dfs(child, board, i - 1, j)
                self.dfs(child, board, i, j + 1)
                self.dfs(child, board, i, j - 1)
                board[i][j] = char


