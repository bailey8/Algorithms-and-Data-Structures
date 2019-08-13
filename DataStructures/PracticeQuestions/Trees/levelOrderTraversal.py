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
        while len(queue) > 0:
            node, level = queue.pop(0)
            ans[level].append(node.val)
            if node.left: queue.append([node.left,level+1])
            if node.right: queue.append([node.right,level+1])
        return ans.values()

        
