def cycle(edges):
 
    # THIS ACTS LIKE OUR GLOBAL VISITED SET IN NORMAL DFS

    black = set()

    def dfsHelper(node,parent):
        
        black.add(node)
        for neigh in graph[node]:
            # If the node has been visited, and is not the parent, then cycle
            if neigh in black and neigh is not parent: return True
            # explore the node if it has not been seen and return cycle result from this dfs
            if neigh not in black and dfsHelper(neigh,node): return True

        return False
    
    import collections
    graph = collections.defaultdict(list)

    for left, right in edges:
        graph[left].append(right)
        graph[right].append(left)

    for node in graph:
        # BLACK SET ACTS LIKE VISITED SET
        if node not in black:
            if dfsHelper(node,None):
                return True
    return False
        

print(cycle([[1,2],[2,3],[1,4],[5,6],[1,6],[5,1]]))