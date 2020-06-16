
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        
        
         # CHECK TO SEE IF THE TREE IS VALID
        def check(tree1, tree2):
            if not tree1 and not tree2: return True
            if not tree1 or not tree2: return False
            return tree1.val == tree2.val
        
        stack = [(p,q)]
        
        # START DFS
        while stack:
            p,q = stack.pop()
            
            #IF THEY ARE NOT EQUAL, RETURN FALSE INDICATING BAD TREE
            if not check(p,q):
                return False
            
            # AT THIS PPOINT WE KNOW THEY ARE EQUAL, SO IF P IS VALID SO IS Q
            if p:  
                stack.append((p.right,q.right))
                stack.append((p.left,q.left))

             
        return True
            

class Solution3:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # CASE IF BOTH ARE NULL: ALL GOOD
        if not p and not q: return True
        
        # CASE IF 1 IS NULL AND OTHER ISNT: NOT GOOD
        if not p or not q: return False
        
        # CASE IF VALUES ARE NOT THE SAME: NOT GOOD
        if p.val != q.val: return False
        
        # IF THEY ARE THE SAME THEN RETURN TRUE
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
     
    
        def validate(root1,root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            
            # VALIDATE BRANCHES BEFORE CHECKING ROOTS
            if not validate(root1.left,root2.left):return False
            if not validate(root1.right,root2.right):return False
            
            return root1.val == root2.val
        
        return validate(p,q)
        