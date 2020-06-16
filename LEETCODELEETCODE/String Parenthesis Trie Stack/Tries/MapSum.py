# class TrieNode:
#     def __init__(self):
#         self.sum = 0
#         self.children = collections.defaultdict(TrieNode)
# class MapSum:

#     def __init__(self):
#         self.root = TrieNode()
        

#     def insert(self, key: str, val: int) -> None:
#         curr = self.root
#         for char in key:
#             curr = curr.children[char]
#         curr.sum = val
        

#     def sum(self, prefix: str) -> int:
        
#         def dfs(curr):
            
#             nonlocal total
#             total += curr.sum
#             for child in curr.children.values(): dfs(child)
                
#         # DIG TO THE END OF THE PREFIX
#         curr = self.root
#         for char in prefix:
#             if char not in curr.children: return 0
#             curr = curr.children[char]
        
#         total = 0
#         # GATHER THE SUMS!!
#         dfs(curr)
#         return total
        

import collections
class MapSum:

    def __init__(self):
        self.map = collections.defaultdict(int)
        self.count = collections.defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        
        # WE WILL NEED TO UPDATE THE VALUE OF EVERY
        # VALUE AT THE CURRENT PREFIX TO THE LEFT TO REFLECT
        # THAT THE "CHAIN" EITHER LOST OR GAINED VALUE
        diff = val - self.map[key]
        self.map[key] = val
        
        for end in range(len(key)+1):
            
            # EVERY WORD THAT IS A PREFIX TO THIS WORD, UPDATE THE VALUE
            self.count[key[:end]] += diff

    def sum(self, prefix: str) -> int:
        return self.count[prefix]

 

 

# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("a",3)
print(obj.map.values())
print(obj.count.values())

print(obj.insert("aa", 2))
print(obj.map.values())
print(obj.count.values())

print(obj.insert("aaa", 5))
print(obj.map.values())
print(obj.count.values())

print(obj.insert("aaaa", 4))
print(obj.map.values())
print(obj.count.values())




