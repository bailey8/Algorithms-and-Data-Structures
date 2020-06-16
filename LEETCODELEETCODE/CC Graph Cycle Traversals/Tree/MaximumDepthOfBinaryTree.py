 

class Solution2(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.right),self.maxDepth(root.left))

# Depth of last node will be the greatest
class BFS(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [(root,1),]
        while queue:
            node, val = queue.pop(0)
            if node.left:
                queue.append((node.left, val+1),)
            if node.right:
                queue.append((node.right, val+1),)
            if not queue:
                return val

class IterativeDFS(object):
    def maxDepth(self, root):
        stack = []
        if not root:
            return 0
        stack.append((1, root),)
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth