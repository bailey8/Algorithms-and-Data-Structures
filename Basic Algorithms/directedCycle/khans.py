import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
         # ONLY TRACKING THE NUMBER OF INCOMING EDGES - NOT SPECIFIC EDGES
        # ONLY TRACKING THE NUMBER OF INCOMING EDGES - NOT SPECIFIC EDGES
        incoming = collections.defaultdict(int)
        outgoing = collections.defaultdict(set)
        for i, j in prerequisites:
            incoming[i] +=1
            outgoing[j].add(i)

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
                if not incoming[neigh]:
                    stack.append(neigh)

            # NO MORE PREREQS SO REMOVE FROM INCOMING OR "PREREQ LIST"
            incoming.pop(node)
        
        # If theres no nodes with incoming edges at the end we know no cycles
        return not incoming