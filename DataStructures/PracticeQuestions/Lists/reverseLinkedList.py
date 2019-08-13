class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            #Save next pointer
            saved = curr.next
            #change pointer of node to previous node
            curr.next = prev
            #make previous node next node for next iteration
            prev = curr
            #make current node the next node we saved off
            curr = saved
        #Return the prev node bc the curr node wiill be None
        return prev

# recurse down to one node then return that node
# Tack on the next node after the node returned,
# Return new head of list which is the last node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        reversed = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed