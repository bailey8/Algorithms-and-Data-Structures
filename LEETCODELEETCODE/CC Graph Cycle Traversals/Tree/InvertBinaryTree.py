# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # BASE CASE, RETURN NONE
        if not root: return None
        
        
        leftBranch = self.invertTree(root.right)
        rightBranch = self.invertTree(root.left)
        
        #BY SWAPPING THE NODES FROM THE BOTTOM UP, WE GET THE INVERTED TREE
        root.right = rightBranch
        root.left = leftBranch
        
        return root
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution2:
    def invertTree(self, root):
        
        queue = collections.deque([root])
        
        # USE BFS TO DO THIS
        while queue:
            
            #POP FROM THE LEFT FOR O(1) TIME
            node = queue.popleft()
            
            #IF WE DIDNT HIT A LEAVE THEN KEEP SWAPPING
            if node:
                node.right,node.left = node.left,node.right
                queue.append(node.right)
                queue.append(node.left)
                
        return root
