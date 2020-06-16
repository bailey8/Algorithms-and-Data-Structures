
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # valid if isValid(root.left) and isValid(root.right)
        
        def bst_helper(node, lower = float('-inf'), upper = float('inf')):
            
            #A NULL NODE IS ALWAYS A VALID BST - BASE CASE
            if not node: return True
            
            # THESE CASES WILL TERMINATE OUR RECURSION EARLY
            #If our node is greater than the maximum value, return False
            if node.val <= lower or node.val >= upper: return False
            
            # To the right side of the tree, it is only valid if the node is greater than it
            return bst_helper(node.right,node.val,upper) and bst_helper(node.left,lower,node.val)
            
         
        
        return bst_helper(root)
  
  

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, minn, maxx = stack.pop()
            # DON'T WORRY ABOUT NULL NODES
            if node:
                #IF IT IS VALID, THEN ADD BOTH CHILDREN, WE CHECK IF THE
                # CHILDREN ARE VALID THE "NEXT" ITERATION!!
                if minn < node.val < maxx:
                    stack.append((node.right, node.val,maxx))
                    stack.append((node.left,minn,node.val))
                else: 
                    return False

        return True
        
        
     
    
    class Solution4:
        def isValidBST(self, root: TreeNode) -> bool:
            arr = []
            def in_order(node):
                if node:
                    in_order(node.left)
                    arr.append(node.val)
                    in_order(node.right)
            in_order(root)
            for i in range(0,len(arr)-1):
                if arr[i] >= arr[i+1]: return False
            return True
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
      
        def dfs(small, large, node):
            
            if not node: return True
            if small < node.val < large: return dfs(small,node.val, node.left) and dfs(node.val,large,node.right)
            return False
        
        return dfs(float('-inf'), float('inf'), root)
     