from collections import defaultdict
class Node:
    def __init__(self):
        self.graph = defaultdict(list)

    def insert(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

# THE RETURNED VISITED SET CAN BE USED TO FIND THE CC
def DFS(graph, start):
    visited = set()
    stack = [start]

    #WHILE YOU STILL HAVE UNVISITED NODES
    while stack:

        #TAKE THE MOST RECENT CHILD THAT WAS ADDED (DEEPEST)
        start = stack.pop()

        #MARK IT AS VISITED BC WE ABOUT TO VISIT ALL ITS CHILDREN
        visited.add(start)
        print(start, end = " ")

        #ADD THE CHILDREN OF THE NODE TO THE STACK SO WE CAN VISIT THEM NEXT
        for child in graph[start]:
            if child not in visited:
                stack.append(child)

    return visited


# THE RETURNED VISITED SET CAN BE USED TO FIND THE CC
def DFSRecursive(graph,start, visited = set()):
    
    #MARK AS VISITED BC WE ARE ABOUT TO VISIT ALL OF ITS NEIGHBORS
    visited.add(start)
    print(start, end = " ")

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





graph = Node()
graph.insert(1,5)
graph.insert(5,4)
graph.insert(1,4)
graph.insert(1,3)
graph.insert(1,2)
graph.insert(2,100)
graph.insert(2,200)
graph.insert(3,1000)
graph.insert(3,2000)
graph.insert(55,53)
graph.insert(223,2342)
graph.insert(223,3019291023)

DFS(graph.graph,1)
print()
DFSRecursive(graph.graph,1)
print()
print(cycle(graph.graph))