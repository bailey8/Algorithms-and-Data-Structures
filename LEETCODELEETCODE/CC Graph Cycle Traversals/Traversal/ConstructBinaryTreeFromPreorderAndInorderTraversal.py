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


from collections import deque
class Solution2:
    def buildTree(self, preorder, inorder):
        
        def helper(left_InOrder,right_InOrder):

            # TIME TO MOVE ON TO THE NEXT SUBTREE
            if left_InOrder > right_InOrder:
                return None

            else:
                # THE VALUE FOR THE ROOT OF THIS SUBTREE -> NEXT ELEMENT IN PREORDER
                root_val = preorder.pop() #if using deque use preorder.popleft()
                root = TreeNode(root_val)

                #CONSTRUCT THE LEFT AND RIGHT SUBTREES
                root.left = helper(left_InOrder, valueToIndex[root_val] - 1)
                root.right = helper(valueToIndex[root_val] + 1, right_InOrder)

                return root

        # MAKE HASHMAP TO GET O(1) ACCESS
        valueToIndex = {value:index for index, value in enumerate(inorder)}
        
        #reverse to pop off the end O(1)
        preorder.reverse()   #if using deque do preorder = deque(preorder)
        
        # preorder = deque(preorder)
        return helper(0,len(inorder)-1)

test = Solution2()
test.buildTree([3,9,20,15,7],[9,3,15,20,7])




