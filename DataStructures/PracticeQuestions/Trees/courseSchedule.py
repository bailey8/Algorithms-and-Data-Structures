# DFS Kahns
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import  defaultdict
    # DFS: from the front to the end    
        incoming = defaultdict(set)
        outgoing = defaultdict(set)
        for i, j in prerequisites:
            incoming[i].add(j)
            outgoing[j].add(i)
        stack = [node for node in range(numCourses) if not incoming[node]]
        while stack:
            node = stack.pop()
            for neigh in outgoing[node]:
                incoming[neigh].remove(node)
                if not incoming[neigh]:
                    stack.append(neigh)
            incoming.pop(node)
        # If theres no nodes with incoming edges at the end we know no cycles
        return not incoming

# BFS with counter
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import  defaultdict
    # DFS: from the front to the end    
        incoming = defaultdict(int)
        outgoing = defaultdict(set)
        for i, j in prerequisites:
            incoming[i] +=1
            outgoing[j].add(i)
        queue = [node for node in range(numCourses) if not incoming[node]]
        while queue:
            node = queue.pop()
            # PUT NODE NEXT IN TOPOLOGICAL ORDERING HERE
            for neigh in outgoing[node]:
                incoming[neigh] -=1
                if not incoming[neigh]:
                    queue.append(neigh)
            incoming.pop(node)
        # If theres no nodes with incoming edges at the end we know no cycles
        return not incoming

# DFS
# class Solution3(object):
#     def canFinish(self, numCourses, prerequisites):
#         from collections import  defaultdict
#     # DFS: from the front to the end    
#         incoming = defaultdict(int)
#         outgoing = defaultdict(set)
#         for i, j in prerequisites:
#             incoming[i] +=1
#             outgoing[j].add(i)
#         queue = [node for node in range(numCourses) if not incoming[node]]
#         while queue:
#             node = queue.pop()
#             # PUT NODE NEXT IN TOPOLOGICAL ORDERING HERE
#             for neigh in outgoing[node]:
#                 incoming[neigh] -=1
#                 if not incoming[neigh]:
#                     queue.append(neigh)
#             incoming.pop(node)
#         # If theres no nodes with incoming edges at the end we know no cycles
#         return not incoming