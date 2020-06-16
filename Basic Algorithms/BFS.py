from collections import defaultdict
class Node:
    def __init__(self):
        self.graph = defaultdict(list)

    def insert(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

# THE RETURNED VISITED SET CAN BE USED TO FIND THE CC
def BFS(graph, start):
    visited = set()
    queue = [start]

    #WHILE YOU STILL HAVE UNVISITED NODES
    while queue:

        #TAKE THE OLDEST CHILD THAT WAS ADDED (SHALLOWEST)
        start = queue.pop(0)

        #MARK IT AS VISITED BC WE ABOUT TO VISIT ALL ITS CHILDREN
        visited.add(start)
        print(start, end = " ")

        #ADD THE CHILDREN OF THE NODE TO THE STACK SO WE CAN VISIT THEM NEXT
        for child in graph[start]:
            if child not in visited:
                queue.append(child)

    return visited

# THE RETURNED VISITED SET CAN BE USED TO FIND THE CC
def BFS_SHORTESTPATH(graph, start):
    visited = set()
    queue = [start]

    #This will store the parent for each node
    parent = defaultdict(lambda: None)

    #WHILE YOU STILL HAVE UNVISITED NODES
    while queue:

        #TAKE THE OLDEST CHILD THAT WAS ADDED (SHALLOWEST)
        start = queue.pop(0)

        #MARK IT AS VISITED BC WE ABOUT TO VISIT ALL ITS CHILDREN
        visited.add(start)

        #ADD THE CHILDREN OF THE NODE TO THE STACK SO WE CAN VISIT THEM NEXT
        for child in graph[start]:
            if child not in visited:
                queue.append(child)

                # RECORD THE CHILDS PARENT SO WE CAN USE IT WHILE CALCULATING SHORTEST PATH
                parent[child] = start

    return parent

def findShortestPath(graph,start,target):

    #FIRST GET THE DICTIONARY THAT CONTAINS ALL THE PARENTS
    parent = BFS_SHORTESTPATH(graph,start)

    # THIS IS TO STORE THE SHORTEST PATH OF THE TARGET NODE
    path = [target]

    # IF THE NODE HAS A PARENT THEN ADD PARENT TO PATH
    while parent[target]:
        # IF THE NODE HAS NO PARENT, THEN WE REACHED THE ROOT NODE
        target = parent[target]

        # ADD THE PARENT TO THE NEXT STEP IN SHORTEST PATH
        path.append(target)

    print(f'The shortest path is: {path} and it has length {len(path)}')
        




graph = Node()
graph.insert(1,5)
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
print()
findShortestPath(graph.graph,1,200)