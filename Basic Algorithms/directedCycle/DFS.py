# DFS
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

# DFS - IDEAL
import collections
class Solution:
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
        
        # ITERATE OVER ALL NODES - MUST BE RANGE HERE!!!
        for node in range(numCourses):
            
            # ONLY EXPLORE THE VISITED NODES
            if node not in black:
                if not dfs(node): 
                    return False
         
        return True