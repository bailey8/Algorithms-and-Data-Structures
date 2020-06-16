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
        topOrder = []

        # ADD ALL THE NODES WITH NO INCOMING EDGES
        def dfs(node):
            grey.add(node)
            
            for neigh in outgoing[node]:
                if neigh in grey: return False
                if neigh in black: continue
                if not dfs(neigh): return False
            
            grey.remove(node)
            black.add(node)

            #NOW THAT WE HAVE EXPLORED ALL NEIGHBORS, ADD IT TO THE TOPSORT
            topOrder.append(node)
            return True
        
        # ITERATE OVER ALL NODES
        for node in range(numCourses):
            
            # ONLY EXPLORE THE VISITED NODES
            if node not in black:
                if not dfs(node): 
                    return False
         
        topOrder.reverse()
        return topOrder

print(Solution5().canFinish(11,[[1,0],[2,1],[3,2],[5,10]])) # [10, 9, 8, 7, 6, 5, 4, 0, 1, 2, 3]



def printy(x):
    print(x)

a = [1,2,3,4,5,6,7]

map(printy,a) # NOTHING HAPPENS, we didnt even capture the generator
list(map(printy,a)) # capture the generator and consume it in one swoop. Prints 1,2,3,4,5,6,7

gen = map(printy,a) # CAPTURE THE GENERATOR
next(gen) #prints 1
next(gen) #prints 2
list(gen) # consumes the generator, so it prints 3,4,5,6,7