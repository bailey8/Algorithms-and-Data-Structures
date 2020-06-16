# from collections import defaultdict
# class TrieNode():
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.isWord = False
    
# class WordDictionary(object):
#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word):
#         node = self.root
#         for w in word:
#             node = node.children[w]
#         node.isWord = True

#     def search(self, word):
#         node = self.root
#         self.res = False
#         self.dfs(node, word)
#         return self.res
    
#     def dfs(self, node, word):
#         if not word:
#             if node.isWord:
#                 self.res = True
#             return 
#         if word[0] == ".":
#             for n in node.children.values():
#                 self.dfs(n, word[1:])
#         else:
#             node = node.children.get(word[0])
#             if not node:
#                 return 
#             self.dfs(node, word[1:])

import collections
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    # STANDARD TRIE ADD WORD METHOD
    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.children[char]
        current.isWord = True
        

    def search(self, word: str) -> bool:
        # GLOBAL FLAG THAT DFS WILL SET IF THE WORD IS VALID
        self.valid = False
        self.dfs(self.root,word,0)
        return self.valid
    
    def dfs(self,node,word,position):
        
        #IF WE FINISHED PROCESSING THE WORD, THEN LETS CHECK IF THE NODE WE LANDED ON IS "ACTUALLY A WORD"
        if position == len(word): 
            # IF THE NODE IS A WORD THEN SET THE GLOBAL FLAG TO TRUE
            if node.isWord: self.valid = True
            return
        
        #THIS IS THE WILDCARD. THIS SHOULD MATCH ANYTHING, SO CALL DFS ON ALL THE CHILDREN
        if word[position] == ".":
            for child in node.children.values():
                #INCREMENT THE STRING INDEX BC WE JUST PROCESSED A LETTER
                self.dfs(child,word,position+1)
        #IF NOT WILDCARD, SEE IF THERE IS A VALID CHILD
        child = node.children.get(word[position])
        #IF THERE IS, WE CONTINUE OUR SEARCH
        if child: self.dfs(child,word,position+1)

        