class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root,float('-inf'),float('inf'))
    def helper(self,root,lower,upper):
        if not root:
            return True
        val = root.val
        if val >= upper or val <= lower:
            return False
        return self.helper(root.right,val,upper) and self.helper(root.left,lower,val)
  
  
class Solution:
    def isValidBST2(self, root: TreeNode) -> bool:
        if not root: return True
        stack = [(root,float("-inf"),float("inf")),]
        while stack:
            root, left, right = stack.pop()

            if not root:
                continue
            if root.val <= left  or root.val >= right:
                return False
            stack.append((root.left,left,root.val),)
            stack.append((root.right,root.val,right),)
        return True

    class Solution:
        def isValidBST(self, root: TreeNode) -> bool:
            stack = []
            mini = float('-inf')
            while True:
                #Add all right nodes until no more
                if root:
                    stack.append(root)
                    root = root.left
                #If nodes left, pop the left most, print it, then go right
                elif stack:
                    root = stack.pop()
                    if root.val <= mini:
                        return False
                    #Set value the next element must be greater than
                    mini = root.val
                    root = root.right
                else:
                    break
            return True
 