from collections import defaultdict

def cycle(edgeList):
    graph = defaultdict(list)
    for i,j in edgeList:
        graph[i].append(j)
        graph[j].append(i)
    
    visited = set()
    cycle = []

    def dfs(node,parent,stack):
        stack.append(node)
        visited.add(node)
        for neigh in graph[node]:
            #check to make sure not parent
            if neigh in visited:
                if neigh != parent[node]:
                    cycle.append(neigh)
                    top = stack.pop()
                    while top != neigh:
                        cycle.append(top)
                        top = stack.pop()
                    return cycle
            else: 
                parent[neigh] = node
                results = dfs(neigh,parent,stack)
                if results: return results
        stack.pop()
        return False

    for node in graph:
        if node not in visited:
            result = dfs(node,{node:None},[])
            if result:
                return cycle
    return [7]

edge = [[100,1],[1,2],[3,99],[2,111],[2,3],[3,1],[4,6]]
print(cycle(edge))
        

    