from collections import defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(v):
            visited.add(v)
            for child in graph[v]:
                if child not in visited:
                    dfs(child)
                    
        graph = defaultdict(set)
        visited = set()
        count = 0
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        for i in range(n):
            if not i in visited:
                count +=1
                dfs(i)
        return count
                
# Weird count way
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/266228/Python-DFSBFSUF
def countComponents(n, edges):
    graph = defaultdict(set)
    visited = set()
    for u, v in edges: 
        graph[u].add(v), graph[v].add(u)

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                dfs(child)
        return 1

    return sum(dfs(i) for i in range(n) if i not in visited)
 
 # ----------------------------------------------------------------------------------
def countComponents2(n, edges):
        # [1,2,3,5,5,6] - Parents 
        def find(node):
            # If the node is not group it started in, find true parent
            if parent[node] != node:
                # Use the nodes parent if the nodes parent isnt actually matching the node
                parent[node] = find(parent[node])
            return parent[node]
            
        def union(xy):
            left, right = map(find, xy)
            # Merge smaller component into larger component
            if rank[left] < rank[right]:
                parent[left] = right
            else:
                parent[right] = left
                if rank[left] == rank[right]:
                    rank[left] += 1
        
        # The groups that each node belongs to!!
        parent = [i for i in range(n)]
        rank = [0] * n
        for edge in edges:
            union(edge)
        return len({find(x) for x in parent})

# QUICKFIND O (N*M) for M union operations on N elements
def countComponents3(n,edges):
    def union(xy):
        x,y = xy
        # All nodes that belonged to previous group, transfer them to new group
        keep = parent[x]
        swap = parent[y]
        for i in range(len(parent)):
            if parent[i] == swap:
                parent[i] = keep

    def find(node1,node2):
        return parent[node1] == parent[node2]
    parent = [i for i in range(n)]
    for edge in edges:
        union(edge)
    return len([i for i in range(len(parent)) if i == parent[i]])



# QUICK - UNION
class Solution4:
    def countComponents(self,n,edges):
        # Time proportional to depth of p and q
        def union(xy):
            x,y = xy
            leftParent = findRoot(x)
            rightParent = findRoot(y)
            parent[leftParent] = rightParent
        # time propertional to DEPTH of i
        def findRoot(node):
            while node != parent[node]: node = parent[node]
            return node
        def find(node1,node2):
            return findRoot(node1) == findRoot(node2)
        parent = [i for i in range(n)]
        for edge in edges:
            union(edge)
        return len([i for i in range(len(parent)) if i == parent[i]])





# WWEIGHTED QUICK UNION
class Solution5:
    def WeightedQuickUnion(self,n,edges):
        # Time proportional to depth of p and q
        def union(xy):
            x,y = xy
            leftParent = find(x)
            rightParent = find(y)
            if size[leftParent] < size[rightParent]:
                parent[leftParent] = rightParent
                size[rightParent] += size[leftParent]
            else:
                parent[rightParent] = leftParent
                size[leftParent] += size[rightParent]
        # time propertional to DEPTH of i
        def find(node):
            while node != parent[node]: node = parent[node]
            return node

        parent = [i for i in range(n)]
        size = [1]*n
        for edge in edges:
            union(edge)
        count = 0
        return len([i for i in range(len(parent)) if i == parent[i]])


print(Solution5().WeightedQuickUnion(5,[[0,1],[1,2],[3,4]]))


# Path Compression
def countComponents5(n,edges):
    # Time proportional to depth of p and q
    def union(xy):
        x,y = xy
        leftParent = find(x)
        rightParent = find(y)
        if size[leftParent] < size[rightParent]:
            parent[leftParent] = rightParent
            size[rightParent] += size[leftParent]
        else:
            parent[rightParent] = leftParent
            size[leftParent] += size[rightParent]
    # time propertional to DEPTH of i
    def find(node):
        while node != parent[node]:
            # Make every other node in path point to grandparent
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    parent = [i for i in range(n)]
    size = [1]*n
    for edge in edges:
        union(edge)
    return len([i for i in range(len(parent)) if i == parent[i]])


class Solution99:
    def countComponents(self, n, edges):
        
        def findRoot(node):
                # WHILE WE HAVENT FOUND THE ROOT OF THE FOREST
                while node != parent[node]:
                    
                    # MAKE THE PARENT OF THIS NODE BECOME THE GRANDPARENT OF THIS NODE
                    parent[node] = parent[parent[node]]
                    #SET THE NODE TO ITS GRANDPARENT
                    node = parent[node]
                #RETURN THE ROOT
                return node
            
        def union(xy):
            x,y = xy
            
            #FIND THE LEADERS OF BOTH THE FOREST THAT THESE 2 NODES RESIDE IN
            root1 = findRoot(x)
            root2 = findRoot(y)
            
            # IF THE LEFT FOREST IS DEEPER THAN RIGHT FOREST, ADD THE RIGHT FOREST TO THE LEFT (BIGGER) FOREST
            if size[root1] > size[root2]:
                parent[root2] = root1
                # add the number of nodes in the right forest to the size of the left forest bc the forests are merged now
                size[root1] += root2
            
            # IF THE RIGHT FOREST IS DEEPER THAN THE LEFT FOREST, THEN ADD THE LEFT FOREST TO THE RIGHT FOREST
            else:
                parent[root1] = root2
                # add the number of nodes in the left forest to the size of the right forest bc the forests are merged now
                size[root2] += size[root1]
            
        
        #EACH NODE STARTS AS A 1 NODE FOREST WHERE EACH NODE IS ITS OWN LEADER
        parent = [i for i in range(n)] 
        # EACH FOREST STARTS OUT WITH A SIZE OF 1
        size = [1 for i in range(n)]
        # APPLY UNION TO EACH EDGE
        for edge in edges:
            union(edge)
            
        #COUNT ALL THE NODES THAT ARE ROOTS OF THE FORESTS THEY LIVE IN. EACH ROOT IS ITS OWN FOREST
        return len([i for i in range(len(parent)) if parent[i] == i])
                
                




 