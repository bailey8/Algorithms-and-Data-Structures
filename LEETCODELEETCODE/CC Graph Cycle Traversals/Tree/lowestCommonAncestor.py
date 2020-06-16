
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        queue = collections.deque([(root,[root])])
        
        paths = list()
        while queue:
            
            if len(paths) == 2: break
                
            node, path = queue.popleft()
            if node:
                
                # IF THEY BOTH MATCH THEN ADD BOTH THE PATHS TO THE OUTPUT
                if node == p and node == q:
                    paths.append(path)
                    paths.append(path)
                
                #IF ONLY ONE MATCHES THEN JUST ADD 1
                elif node == q or node == p:
                    paths.append(path)
                
                # ADD THE CHILDREN
                queue.append((node.left, path + [node.left]))
                queue.append((node.right, path + [node.right]))
            
        for i,j in reversed(list(zip(paths[0],paths[1]))):
            if i==j: return i
                
# [3,5,1,6,2,0,8,null,null,7,4]
# 5
# 1

root = TreeNode(3)
root.right = TreeNode(5)
root.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right= TreeNode(4)

print(Solution().lowestCommonAncestor(root, root.left,root.right))


import collections
class Solution:
    
    def __init__(self):
        self.flag = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def dfs(node = root):
            
            if not node: return False
            
            # THIS IS A BASE CASE IN A WAY
            midNodeFound = node == p or node == q
            
            # FIRST SEE IF THE SECOND MATCHING NODE IS DEEPER IN THIS SAME SUBTREE
            rightNodeFound = dfs(node.right)
            leftNodeFound = dfs(node.left)
            
            
            # BOOLEAN ADDITION. COOL! THIS WILL BE TRUE IF THE NODE WE ARE AT IS THE 
            # LOWEST COMMON ANCESTOR.
            if rightNodeFound + leftNodeFound + midNodeFound >= 2: self.flag = node
                
            #IF THE SECOND MATCHING NODE IS NOT DEEPER IN THE SUBTREE, THEN SIGNAL
            # THAT ONE OF THE NODES WAS FOUND, AND THEN LOOK FOR THE OTHER HIGHER UP
            return rightNodeFound or leftNodeFound or midNodeFound
            
        dfs()
        return self.flag
  
                

               