class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left,root.right = right,left
        return root

class Solution(object):
    def invertTree(self, root):
        if not root: return None
        queue = [root]
        while queue:
            curr = queue.pop(0)
            curr.right,curr.left = curr.left,curr.right
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        return root