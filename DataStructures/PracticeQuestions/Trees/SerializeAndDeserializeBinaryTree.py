# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Codec:
#     def serialize(self, root):
#         def helper(root,string):
#             if root is None:
#                  string += "None,"
#             # We want to serialize left nodes first
#             else:
#                 string += str(root.val) + ","
#                 string = helper(root.left,string)
#                 string = helper(root.right,string)
#             return string
#         return helper(root,'')
        

#     def deserialize(self, data):
#         nodes = data.split(",")
#         def helper(arr):
#             if arr[0] == "None":
#                 arr.pop(0)
#                 return None
#             temp = TreeNode(arr[0])
#             arr.pop(0)
#             temp.left = helper(arr)
#             # By the time this is reached, the list will only contain the right nodes
#             temp.right = helper(arr)
#             return temp
#         return helper(nodes)

# class Codec:
#     def serialize(self, root):
#         arr = []
#         def helper(root):
#             if root is None:
#                  arr.append("#")
#             # We want to serialize left nodes first
#             else:
#                 arr.append(str(root.val))
#                 helper(root.left)
#                 helper(root.right)
#         helper(root)
#         return " ".join(arr)

#     def deserialize(self, data):
#         nodes = data.split(" ")
#         def helper():
#             if nodes[0] == "#":
#                 nodes.pop(0)
#                 return None
#             node = TreeNode(nodes.pop(0))
#             node.left = helper()
#             # By the time this is reached, the list will only contain the right nodes
#             node.right = helper()
#             return node
#         return helper()
class Codec:
    def serialize(self, root):
        preorder = []
        def helper(root):
            if root == None:
                preorder.append("#")
            else:
                preorder.append(str(root.value))
                helper(root.left)
                helper(root.right)
        helper(root)
        return " ".join(preorder)

    def deserialize(self, data):
        nodes = data.split()
        def helper():
            if len(nodes) == 0: return None
            if nodes[0] == "#":
                nodes.pop(0)
                return None
            node = TreeNode(nodes.pop(0))
            node.left = helper()
            nodes.right = helper()
            return node
        return helper()
        


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))