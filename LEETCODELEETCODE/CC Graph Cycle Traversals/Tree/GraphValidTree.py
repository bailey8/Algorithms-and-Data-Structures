class Solution:
    def validTree(self, n: int, edges) -> bool:
        
        def union(leftNode, rightNode):
            
            leftRoot = findRoot(leftNode)
            rightRoot = findRoot(rightNode)
            
            # IF TWO NODES HAVE THE SAME PARENT AND ARE BING CONNECTED, THEN A CYCLE WILL FORM
            if leftRoot == rightRoot: return False
            
            if size[leftRoot] < size[rightRoot]:
                parent[leftRoot] = rightRoot
                size[rightRoot] += leftRoot
            else:
                parent[rightNode] = leftNode
                size[leftRoot] += rightNode
            return True
            
            
        def findRoot(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        
        for leftNode, rightNode in edges:
            if not union(leftNode,rightNode): return False
        
        # if len([i for i in range(n) if i == parent[i]]) != 1: return False
        # ALL TREES HAVE N-1  EDGES
        return len(edges) == n-1

print(Solution().validTree(5,[[0,1],[2,3],[3,4],[2,4]]))

class Solution2:
    def validTree(self, n: int, edges) -> bool:

        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v].append(w)
            neighbors[w].append(v)
            
        # MAKE SURE ALL EDGES ARE RMEOVED, BASICALLY THIS CHECKS TO ENDURE THE GRAPH IS ONE CONNECTED COMPONENT    
        def visit(v):
            children = neighbors.pop(v,[])
            for child in children:
                visit(child)
        
        visit(0)
        
        #if there was a cycle, then the edges would not be n-1
        # if there were multiple connected components, then there would be neighbors left
        return len(edges) == n-1 and not neighbors


