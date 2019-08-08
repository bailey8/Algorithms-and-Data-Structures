class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None
##From begining
def removeNthNodeFromList(head,n):
   if n ==1:
       return head.next
   curr = head.next
   prev = head
   count = 1
 
   while count <= n:
       count += 1
       if count == n:
           if curr.next == None:
               prev.next = None
               curr = None
               return head
 
           prev.next = curr.next
           curr = None
           return head
 
       else:
           curr = curr.next
           prev = prev.next
def removeNthFromEnd(head,n):
   if head == None:
        return head
   slow,fast = head,head
   for i in range(n):
       fast = fast.next
   if fast == None:
       return head.next
   while fast.next:
       fast,slow = fast.next,slow.next
