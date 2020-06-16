from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = defaultdict(list)
        queue = []
        queue.append((root,0),)
        level = 0
        while queue:
            node, level = queue.pop(0)
            ans[level].append(node.val)
            if node.left: queue.append([node.left,level+1])
            if node.right: queue.append([node.right,level+1])
        return ans.values()


# BFS EDITION - ABOVE EXAMPLE SLIGHTLY DIFFERENT
import collections
class Solution2:
    def levelOrder(self, root):
        
        answer = collections.defaultdict(list)
        
        # ADD THE LEVEL IN THE QUEUE
        queue = [(root,0)]
        
        # WHILE WE STILL HAVE MORE NODES TO EXPLORE
        while queue:
            node,level = queue.pop(0)
            
            #IF WE HAVENT HIT A LEAF
            if node:
                answer[level].append(node.val)
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))
                
        return answer.values()
        

#recursive 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution3:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = collections.defaultdict(list)
        if not root: return []
        
        def DFS(node, level):

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                DFS(node.left, level + 1)
            if node.right:
                DFS(node.right, level + 1)
            
        DFS(root, 0)
        return levels.values()


class Solution:
    def levelOrder(self, root):
        
        levels = collections.defaultdict(list)  
        
        def dfs(node, level = 0):
            # IF WE HAVE NOT HIT A LEAVE
            if node:
                # APPEND THE NODE'S VALUE TO ITS CORRESPONDING LEVEL
                levels[level].append(node.val)
                #INCREMENT THE LEVEL AND PERFORM DFS UNTIL WE HIT LEAVES
                dfs(node.left, level+1)
                dfs(node.right, level+1)
            
        dfs(root)
        return levels.values()
            
        
        