 class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None

class Solution:
    def __init__(self):
        self.result = set()
        
        
    # FUNCTION TO REGISTER ALL THE WORDS INTO THE TRIE
    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            curr = root
            for letter in word:
                curr = curr.children[letter]
            curr.word = word
        return root

    def findWords(self, board, words):
        # first build the trie
        root = self.buildTrie(words)
        # CALL DFS ON EVERY CELL IN THE MATRIX
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(root, board, i, j)
        return list(self.result)

    def dfs(self, node, board, i,j):
        
        if node.word: self.result.add(node.word)
            
        # BOUNDING FUNCTION -------------------------
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
                 
           

import collections
class TrieNode:
    def __init__(self):
        self.isWord = None
        self.children = collections.defaultdict(TrieNode)


class Solution:
    
    def __init__(self):
        self.root = TrieNode()
        
    def findWords(self, board, words):
        
        def insert(word):
            current = self.root
            for char in word:
                current = current.children[char]
        
            current.isWord = str(word)
            
        def visit(row,col, node = self.root):
            
            # MAKE SURE THE INDEX IS VALID (WE ARE IN THE GRID)
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]): return
            
            # THIS IS THE NEXT CHARACTER WE WILL PROCESS
            currentLetter = board[row][col]
            
            # IF THIS NEW CHAR IS A CHILD OF NODE, THEN WE CAN EXPLORE IT
            if currentLetter in node.children:
                
                # CHANGE OUR NODE TO BE THE "NEW CHARACTER"
                node = node.children[currentLetter]
                 
                    
                #CHECK IF THERE IS A WORD FORMED NOW THAT WE ADDED A CHARACTER
                if node.isWord: wordSet.add(node.isWord)
                    
                
                # TO PREVENT THE RECURSIVE CALLS FROM USING THE LETTER TWICE (LOOP/CYCLE)
                board[row][col] = None
                visit(row-1,col,node)
                visit(row,col-1,node)
                visit(row+1,col,node)
                visit(row,col+1,node)
                board[row][col] = currentLetter
                        
        
        #Insert the words - O(numWords *avgLength(w))
        for word in words:
            insert(word)
        
        wordSet = set()
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                visit(row,col)
                
        return wordSet
                

sol = Solution()
print(sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain"]))