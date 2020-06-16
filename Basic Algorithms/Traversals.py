class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

# PRINT THE LEFT NODE OF ROOT, THEN ROOT, THEN THE RIGHT NODE
def InOrder(root):

    # IF WE HIT A LEAF, THEN CONTINUE AND STOP RECURSING
    if root:
        InOrder(root.left)
        print(root.value,end = " ")
        InOrder(root.right)

def PreOrder(root):
    
    # IF WE HIT A LEAF, THEN CONTINUE AND STOP RECURSING
    if root:

        #Print root and keep digging
        print(root.value, end = " ")
        PreOrder(root.left)
        #after we hit first base case, we call the function on the right node
        PreOrder(root.right)

def postOrder(root):

    # IF WE HIT A LEAF, THEN CONTINUE AND STOP RECURSING
    if root:
        # ENSURE YOU'VE EXPLORED BOTH THE LEFT AND RIGHT SIDE OF YOUR NODE BEFORE PRINTING IT
        postOrder(root.left)
        postOrder(root.right)
        print(root.value, end = " ")
        


def InOrderIterative(root):

    #this is our tracking node
    current = root
    stack = []
    while True:

        # THIS IS THE BASE CASE
        #This means we haven't hit a leave yet
        if current:
            stack.append(current)
            current = current.left

        #THIS IS WHAT WE DO AFTER FIRST RECURSIVE DIVE
        # If this hits that means we are at a leave
        elif stack:

            #Pop most recent node
            current = stack.pop()
            print(current.value, end = " ")
            current = current.right

        else:
            break


#ITERATE OVER ROOT, LEFT, AND THEN RIGHT
def preOrderIterative(root):

    # THIS IS THE STACK TO VISIT THE ROOT NODES WE HAVENT PRINTED
    stack = []
    current = root

    # THIS WILL BREAK WHEN STACK IS EMPTY AND CURRENT IS LEAF (NONE)
    while True:

        #If we haven't hit leaf, then print the node and explore the left side
        #This is preOrder, so we print the root AND THEN explore the left side
        # where with inorder we explore the left side AND THEN print the root
        if current:
            print(current.value, end = " ")
            stack.append(current)
            current = current.left

        #Once we hit leaf node, all we have to do is pop the parent
        # and explore the right side of parent, bc we alreay printed parent
        #above, so we don't have to do it here!!!
        elif stack:
            current = stack.pop()
            # WE ALREADY PRINTED THE PARENT (CURRENT) SO JUST SKIP AHEAD TO RIGHT CHILD
            current = current.right
        else:
            break
            
a = Node(7)
a.insert(5)
a.insert(10)
a.insert(0)
a.insert(6)
a.insert(9)
a.insert(11)


InOrder(a)
print()
PreOrder(a)
print()
preOrderIterative(a)
print()
postOrder(a)
print()
 


    