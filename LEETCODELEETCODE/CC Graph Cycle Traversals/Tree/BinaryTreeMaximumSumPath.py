class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def max_gain(node):
            
            nonlocal maximum
            
            if not node: return 0
 
            # max sum on the left and right sub-trees of node
            left_max  = max(max_gain(node.left),0)
            right_max = max(max_gain(node.right),0)
            
            # the price to start a new path where `node` is a highest node
            # update max_sum if it's better to start a new pat
            maximum = max(maximum, right_max + left_max + node.val)
           
            # THE PARENT CAN ONLY FOLLOW ONE OF THE PATHS, SO RETURN THE GREATEST ONE    
            return node.val + max(right_max, left_max)
        
        # THIS IS THE RUNNING TOTAL FOR THE MAX PATH LENGTH
        maximum = float('-inf')
        max_gain(root)
        return maximum
 
