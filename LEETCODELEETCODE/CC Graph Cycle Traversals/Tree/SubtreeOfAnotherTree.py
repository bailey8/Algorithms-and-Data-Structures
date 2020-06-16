# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, a, b):
        
        # SIMPLE CODE TO VALIDATE TREE
        def checkTree(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2 or root2 and not root1:
                return False
            
            if root1.val != root2.val:
                return False
            
            return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)
        
        def dfs(s, t):
            #BASE CASE
            if not s: return False
            
            # IF THE TREE IS VALID, THEN WE GOOD
            if s.val == t.val and checkTree(s, t): return True
            
            #IF ONE SUBTREE CONTAINS THE DESIRED TREE, THEN WE ARE ALL SET
            return dfs(s.left, t) or dfs(s.right, t)
            
        return dfs(a, b)


class Solution2:
    def isSubtree(self, s, t) -> bool:
        
        def findNode(node,target):
            if not node: return None
            if node.val == target.val: return node
            
            if target.val < node.val: 
                return findNode(node.left, target)
            else: 
                return findNode(node.right,target)
        
        def verify(real, copy):
            if not real and copy or not copy and real: return False
            if not copy: return True
            if real.val != copy.val: return False
            
            return verify(real.left,copy.left) and verify(real.right,copy.right)
        
        node = findNode(s,t)
        return verify(node,t)