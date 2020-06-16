 
import collections
# KHANS - COUNTER VERISON
class Solution2:
    def canFinish(self, numCourses: int, prerequisites):
    
         # ONLY TRACKING THE NUMBER OF INCOMING EDGES - NOT SPECIFIC EDGES
        # ONLY TRACKING THE NUMBER OF INCOMING EDGES - NOT SPECIFIC EDGES
        incoming = collections.defaultdict(int)
        outgoing = collections.defaultdict(set)

        for course, preReq in prerequisites:
            incoming[course] +=1
            outgoing[preReq].add(course)

        # ADD ALL THE NODES WITH NO INCOMING EDGES
        stack = [node for node in range(numCourses) if not incoming[node]]
        topOrder = []


        # WHILE YOU STILL HAVE A NODE WITH NO INCOMING EDGES LEFT
        while stack:
            node = stack.pop()

            # WE HAVE COMPLETED THIS COURSE, ADD IT TO TOPORDER
            topOrder.append(node)

            #DECREMENT ONE OF THIS NODES PREREQS
            for neigh in outgoing[node]:
                incoming[neigh] -=1

                #If NO more PREREQS then add NEIGH to STACK
                if incoming[neigh] == 0:
                    stack.append(neigh)

            # NO MORE PREREQS SO REMOVE FROM INCOMING OR "PREREQ LIST"
            incoming.pop(node)
        
        # If theres no nodes with incoming edges at the end we know no cycles
        return "cycle" if incoming else topOrder
    
print(Solution2().canFinish(11,[[1,0],[2,1],[3,2],[5,10]])) # [10, 5, 9, 8, 7, 6, 4, 0, 1, 2, 3]





# DFS - NOT IDEAL WAY
import collections
import collections
class Solution4:
    def canFinish(self, numCourses, prerequisites):
    
        outgoing = collections.defaultdict(set)
        
        for course, preReq in prerequisites:
            outgoing[preReq].add(course)
        
        white = {node for node in range(numCourses)}
        
        # OUR TEMP STORAGE TO DETECT NODES THAT ARE BEING VISITED
        grey = set()
        
        # ACTS LIKE OUR VISITED
        black = set()

        # ADD ALL THE NODES WITH NO INCOMING EDGES
        def dfs(node):

            # GOOD USE OF DISCARD
            white.discard(node)
            grey.add(node)
            
            for neigh in outgoing[node]:
                if neigh in grey: return False
                if neigh in black: continue
                if not dfs(neigh): return False
            
            grey.remove(node)
            black.add(node)
            return True
        
        
        while white:
            if not dfs(white.pop()):
                return False
        
        return True
            
            
# DFS - IDEAL WAY
import collections
class Solution5:
    def canFinish(self, numCourses, prerequisites):
    
        incoming = collections.defaultdict(int)
        outgoing = collections.defaultdict(set)
        
        for course, preReq in prerequisites:
            outgoing[preReq].add(course)
                
        # OUR TEMP STORAGE TO DETECT NODES THAT ARE BEING VISITED
        grey = set()
        
        # ACTS LIKE OUR VISITED
        black = set()

        # ADD ALL THE NODES WITH NO INCOMING EDGES
        def dfs(node):
            grey.add(node)
            
            for neigh in outgoing[node]:
                if neigh in grey: return False
                if neigh in black: continue
                if not dfs(neigh): return False
            
            grey.remove(node)
            black.add(node)
            return True
        
        # ITERATE OVER ALL NODES
        for node in range(numCourses):
            
            # ONLY EXPLORE THE VISITED NODES
            if node not in black:
                if not dfs(node): 
                    return False
         
        return True  




