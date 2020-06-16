from collections import defaultdict

def detect(num,edges):
    size = [1]*num
    parent = [i for i in range(num)]

    def union(leftNode,rightNode):

        leftRoot = findRoot(leftNode)
        rightRoot = findRoot(rightNode)   

        if size[leftRoot] < size[rightRoot]:
            parent[leftRoot] = rightRoot
            size[rightRoot] += size[leftRoot]
        else:
            parent[rightRoot] = leftRoot
            size[leftRoot] += size[rightRoot]
        return False
        
    def findRoot(p):
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p=  parent[p]
        return p
    

    #If the NODES ARE IN THE SAME GROUP, AND ANOTHER EDGE CONNECTS THEM, THEN CYCLE
    for leftNode, rightNode in edges: 
        union(leftNode,rightNode)
    
    # return len([i for i in range(num) if parent[i] == i])
    for i in size: print(i)


print(detect(2,[[0,1],[1,0],[1,0]]))
     
