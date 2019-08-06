class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert a new node with the given key 
def insert(root,node): 
#if root is None then the node becomes the root
    if root is None: 
        root = node 
    else: 
        #first check if the value is less than val to determine which way to go (left/right)
        if node.val > root.val:
            #if no right node, then insert it, we done 
            if root.right is None: 
                root.right = node 
            #If right node, call recursivley cause we aint there yet
            else: 
                insert(root.right, node) 
        #cif no left node, insert
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
def search(root,key): 

    # Base Cases: root is null or key is present at root 
    if root is None or root.val == key: 
        return root 
  
    # Key is greater than root's key 
    if key > root.val: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key) 
  



tree = "sdsds"