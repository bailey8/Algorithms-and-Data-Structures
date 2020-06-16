# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        
        #PREORDER DFS TRAVERSAL - ROOT -> LEFT -> RIGHT
        arr = []
        def rserialize(root):
            
            #THIS IS A TREE, SO NO NEED FOR VISITED SET
            if root is None:
                arr.append("None")
                
            else:
                
                # THIS IS PREORDER, SO VISIT ROOT FIRST
                arr.append(str(root.val))
                
                # NEXT VISIT LEFT NODE
                rserialize(root.left)
                
                #LAST VISIT RIGHT NODE
                rserialize(root.right)
        
        rserialize(root)
        return ",".join(arr)
    
 
    def deserialize(self, data):
        
        def convert():
            
            # BASE CASE
            if not data_list: return None
            
            # GET THE NEXT NODE TO INSERT
            nextVal = data_list.popleft()
            
            # IF IT IS NONE, THEN RETURN NONE
            if nextVal == "None": 
                return None
            # IF NOT, THEN MAKE A NODE OUT OF IT AND ADD IT TO YOUR TREE
            else: 
                root = TreeNode(int(nextVal))
                
            root.left = convert()
            root.right = convert()
            return root
            
        # data_list = collections.deque(data.split(","))
        
        # return convert()
        
        

test = ["word1","word2","word3","word4"]
a = list(zip(test,test[1:])) #[('word1', 'word2'), ('word2', 'word3'), ('word3', 'word4')]
for element in a:
    for element2 in zip(*element):
        print(element2)                      #('w', 'w')
        #                                     ('o', 'o')
        #                                     ('r', 'r')
        #                                     ('d', 'd')
        #                                     ('1', '2')
        #                                     ('w', 'w')
        #                                     ('o', 'o')
        #                                     ('r', 'r')
        #                                     ('d', 'd')
        #                                     ('2', '3')
        #                                     ('w', 'w')
        #                                     ('o', 'o')
        #                                     ('r', 'r')
        #                                     ('d', 'd')
        #                                     ('3', '4')



        
        
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
serial = codec.deserialize(codec.serialize(root))

codec = Codec()
# codec.deserialize(codec.serialize(root))

arr = ["1","2","3"]
print(",".join(arr))