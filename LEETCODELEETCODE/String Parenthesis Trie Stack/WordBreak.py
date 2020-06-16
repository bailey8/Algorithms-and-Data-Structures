# import collections
# class TrieNode:
    
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.isWord = False
# class Solution:
    
#     def __init__(self):
#         self.root = TrieNode()
#     def wordBreak(self, s: str, wordDict) -> bool:
        
    
#         def search(node,index):
            
#             if index == len(s): return node.isWord
            
#             child = root = False
            
#             # START BACK UP TOP AT THE ROOT IF WE COMPLETED A WORD, OR KEEP GOING
#             if s[index] in node.children: child = search(node.children[s[index]], index +1) 
#             if node.isWord: root = search(self.root, index)
                
#             return child or root
        
#         for word in wordDict:
#             self.insertWord(word)
#         return search(self.root,0)
        
    
    
#     def insertWord(self, word):
#         current = self.root
#         for char in word:
#             current = current.children[char]
#         current.isWord = True





class Solution:
    
    def wordBreak(self, s: str, wordDict) -> bool:
        
 
        def word_break(startIndex):
        
            # BASE CASE, RETURN TRUE
            if startIndex == len(s): return True;
            
            #CACHE THE SUBPROBLEMS
            if startIndex in cache: return cache[startIndex]
               
            #FOR EVERY POSSIBLE SUBSTRING IN THE FUTURE....
            for end in range(startIndex + 1, len(s)+1):
                
                # IS THERE A WORD THAT WILL SATISFY IT??
                if s[startIndex:end] in wordDict: 
                    #IF THERE IS, THEN EXPLORE AFTER THAT WORD
                    cache[startIndex] = word_break(end)
                    if cache[startIndex]: return True
            
            #IF NOTHING WORKED, THEN RETURN FALSE
            cache[startIndex] = False
            return cache[startIndex]
            
        cache = {}
        return word_break(0)


# VERSION WITH DEFAULTDICT
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        def dfs(index):

            if index == len(s): return True

            #CACHE THE SUBPROBLEMS
            if index in cache: return cache[index]

            for word in wordDict:

                length = len(word)
                substring = s[index:index + length]
                if substring == word:
                    
                    # EXPLORE THE NEXT INDEX AFTER THE WORD YOU JUST USED
                    if dfs(index + len(word)):
                        cache[index] = True
                        break

            #IF NOTHING WORKED, THEN RETURN FALSE
            return cache[index]

        cache = collections.defaultdict(bool)
        return dfs(0)

        
print(Solution().wordBreak("leetcode",["leet","code"]))