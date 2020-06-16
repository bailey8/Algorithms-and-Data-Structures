class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        #If the list is only 1 element or 0 elements, just return the list
        if head == None: return None
        if head.next == None: return None

        #MAKE A TEMP POINTER USED TO GET LENGTH OF THE LINKED LIST
        temp = head

        #GET LENGTH OF LINKED LIST
        count = 1
        while temp.next:
            count += 1
            temp = temp.next
        
        #THIS RETURNS THE INDEX WE WANT TO DELETE
        deleteNodeIndex = count-n
        
        #Range is (inclusive, exclusive) STOP 1 BEFORE DELETE NODE TO CAPTURE NEXT POINTER
        #IF INDEX IS 1, THEN WE WANT TO STOP AT NODE 0.
        temp = head
        for i in range(0,deleteNodeIndex-1):
            temp = temp.next

        #EDGE CASE IS IF DELETE INDEX IS 0 BC THEN WE CANT STOP THE NODE BEFORE
        if deleteNodeIndex == 0:
            return head.next
        
        #EDGE CASE IF WE ARE DELETING THE LAST NODE IN THE LIST
        if temp.next.next == None:
            temp.next = None
            return head
        
        #NORMAL CASE
        temp.next = temp.next.next
        return head



#One pass
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
 
        #If we have to delete the kth node from the end, then we are really deleting the
        # (length - n node from the begining)
        fast = slow = head
    
        # increment to the complement 
        for _ in range(n):
            fast = fast.next
        # if n was len(list) then len(list) - k is 0
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        #delete the node
        slow.next = slow.next.next
        return head
        

solution = Solution()
linkedList = ListNode(1)
linkedList.next = ListNode(2)
head = solution.removeNthFromEnd(linkedList,2)

