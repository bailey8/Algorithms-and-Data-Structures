class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# def mergeTwoLists(self, l1, l2):
#     # If anyone of the lists is exhausted, return the other list
#     if l1 is None: return l2
#     if l2 is None: return l1

#     # Return the smaller of the two nodes passed.
#     # Point smaller node's next to the next smaller
#     # node in the residual lists.
#     if l1.val < l2.val:
#         #l1 is the smallest, so we want to return it
#         l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = self.mergeTwoLists(l1, l2.next)
#         return l2


# # Space Complexity O(1) bc only a few pointers are made
# # Time Complexity O(n+m)
# def mergeTwoListsIter(self, l1, l2):
#     # maintain an unchanging reference to node ahead of the return node.
#     prehead = ListNode(-1)

#     prev = prehead
#     while l1 and l2:
#         if l1.val <= l2.val:
#             prev.next = l1
#             l1 = l1.next
#         else:
#             prev.next = l2
#             l2 = l2.next            
#         prev = prev.next

#     # exactly one of l1 and l2 can be non-null at this point, so connect
#     # the non-null list to the end of the merged list.
#     prev.next = l1 if l1 is not None else l2

#     return prehead.next

def mergeTwoListsIter(self, l1, l2):
    root = ListNode(-1)
    curr = root
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l2 == None else l2
    return root.next

def mergeTwoListsRecursive(self,l1,l2):
    if l1 is None: return l2
    if l2 is None: return l1
    
    if l1.val < l2.val:
        l1.next = self.mergeTwoListsRecursive(l1.next,l2)
        return l1
    else:
        l2.next = self.mergeTwoListsRecursive(l1,l2.next)
        return l2
    


a = {}
b = set()
# b.add([1,2,3])  BAD
b.add((1,2)) # GOOD
a[(1,2,3)] = 99 #GOOD
