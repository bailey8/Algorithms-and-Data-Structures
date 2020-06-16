import collections
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# BFS
def cloneGraph1(self, node):
    if not node:
        return 
    nodeCopy = UndirectedGraphNode(node.label)
    dic = {node: nodeCopy}
    queue = [node]
    while queue:
        node = queue.pop(0)
        for neighbor in node.neighbors:
            if neighbor not in dic: # neighbor is not visited
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                queue.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return nodeCopy
    
# DFS iteratively
def cloneGraph2(self, node):
    if not node:
        return 
    nodeCopy = UndirectedGraphNode(node.label)
    dic = {node: nodeCopy}
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                stack.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return nodeCopy
    
# DFS recursively
def cloneGraph(self, node):
    if not node:
        return 
    nodeCopy = UndirectedGraphNode(node.label)
    dic = {node: nodeCopy}
    self.dfs(node, dic)
    return nodeCopy
    
def dfs(self, node, dic):
    for neighbor in node.neighbors:
        if neighbor not in dic:
            neighborCopy = UndirectedGraphNode(neighbor.label)
            dic[neighbor] = neighborCopy
            dic[node].neighbors.append(neighborCopy)
            self.dfs(neighbor, dic)
        else:
            dic[node].neighbors.append(dic[neighbor])


 
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        
        def dfs(root,copyRoot):
            #FOR ALL NEIGHBORS
            for neigh in root.neighbors:

                if neigh not in visited:
                     #We don't have a clone yet, so we need to create the clone
                    copyNeigh = Node(neigh.val,[])

                    # Now that we have the clone, append it as a neighbor to root
                    copyRoot.neighbors.append(copyNeigh)

                    # Keep track of it in a map so we can reference it later if the neigh was
                    # already visited
                    realToCloneMap[neigh] = copyNeigh

                    # Mark the neeighbor as visited "prep"
                    visited.add(neigh)

                    #Explore this new node
                    dfs(neigh,copyNeigh)
                else:
                    #ADD THE NEIGHBOR TO THE NEIGHBORS ARRAY
                    copyRoot.neighbors.append(realToCloneMap[neigh])

        visited = {node}
        copyRoot = Node(node.val,[])
        realToCloneMap = {node:copyRoot}
        dfs(node,copyRoot)
        
        return copyRoot
        

# THE BEST WAY TO DO IT
class Solution99:
    def cloneGraph(self, node):

        def dfs(root,copyRoot):
        
            for child in root.neighbors:
                
                # we already have created and called dfs on the clone, so just add it as a child and be done with it
                if child in visited: copyRoot.neighbors.append(visited[child])
                else:
                    copyChild = Node(child.val,[])
                    copyRoot.neighbors.append(copyChild)
                    visited[child] = copyChild
                    dfs(child,copyChild)
            
            
        if not node: return None
        newRoot = Node(node.val,[])
        visited = {node:newRoot}
        dfs(node,newRoot)
        return newRoot

 
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

from collections import defaultdict

a = defaultdict(TrieNode)
print(not a[0]) # FALSE
print(not a[0]) # FALSE
print(list(a.values()))
 
a = defaultdict(str) # True
b = defaultdict(list) # True
c = defaultdict(int) # True
d = defaultdict(TrieNode) # False
print(not a[0],not b[0], not c[0],not d[0])