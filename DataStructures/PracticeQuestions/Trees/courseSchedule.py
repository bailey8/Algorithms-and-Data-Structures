#Brute force - check for each node if its in a cycle - O (VE)
# from collections import defaultdict
# def canFinish(self, numCourses, prerequisites):
#     forward = {i: set() for i in range(numCourses)}
#     courses_i_is_a_prereq_for = defaultdict(set)
#     for i, j in prerequisites:
#         # For every course, add the prereq
#         forward[i].add(j)
#         # For every PREREQ, add the courses they unlock. if a node is in here, it means the PREREQ IS BLOCKING IT
#         courses_i_is_a_prereq_for[j].add(i)
#     # Pick every course with no prereqs
#     stack = [node for node in range(numCourses) if not courses_i_is_a_prereq_for[node]]
#     while stack:
#         # Remove first course with no prereqs
#         node = stack.pop()
#         # For EVERY PREREQ
#         for neigh in forward[node]:
#             # delete the POPPED NODE from BLOCKING STATE
#             # Saying.. Hey! I've completed the prereq, so 
#             courses_i_is_a_prereq_for[neigh].remove(node)
#             #
#             if not courses_i_is_a_prereq_for[neigh]:
#                 stack.append(neigh)
#         courses_i_is_a_prereq_for.pop(node)
#     return not courses_i_is_a_prereq_for
 
from collections import  defaultdict
# DFS: from the front to the end    
def canFinish(numCourses, prerequisites):
    forward = {i: set() for i in range(numCourses)}
    backward = defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    stack = [node for node in range(numCourses) if not backward[node]]
    while stack:
        node = stack.pop()
        for neigh in forward[node]:
            backward[neigh].remove(node)
            if not backward[neigh]:
                stack.append(neigh)
        backward.pop(node)
    return not backward

canFinish(4,[[1,0],[3,2]])