
# THE RETURNED VISITED SET CAN BE USED TO FIND THE CC
def DFSRecursive(graph,start, visited = set()):
    
    #MARK AS VISITED BC WE ARE ABOUT TO VISIT ALL OF ITS NEIGHBORS
    visited.add(start)

    for child in graph[start]:
        if child not in visited:
            # KEEP DIGGING UNTIL WE CANT DIG ANYMORE
            DFSRecursive(graph,child,visited)
    return visited


def DFSConnectedComponent(graph):

    #First we need a count of connected components
    count = 0
    
    # Next we need a global visited set
    visited = set()

    #next we start performing DFS on ALL NODES IN THE GRAPH
    for node in graph:
        # Check to see if this node was visited in a previous DFS
        if node not in visited:
            #If we have to start a new DFS that means this is a new CC
            count += 1
            # PERFORM DFS ON THIS NEW COMPONENT WE FOUND
            DFSRecursive(graph,node,visited)
    return count