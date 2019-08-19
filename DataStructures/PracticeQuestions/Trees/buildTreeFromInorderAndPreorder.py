class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            #first element in inorder is root of tree
            ind = inorder.index(preorder.pop(0))
            # Build root with this node
            root = TreeNode(inorder[ind])
            # Pass on the full preOrder and partial inorder
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

test = Solution()
test.buildTree([3,9,20,15,7],[3,9,20,15,7])




