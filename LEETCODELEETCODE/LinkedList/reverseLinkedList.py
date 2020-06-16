class Solution:
    def reverseList(self, head):
        
        headOfList = None
        curr = head
        
        # a -> b -> c -> None
        while curr:
            
            # nextTemp = secondNode (hold: b)
            hold = curr.next
            
            # THE PREVIOUS HEAD NOW COMES AFTER CURRENT (BC WE PUT IT BEFORE FOR REVERSE)
            # PLACE THE NODE BEHIND THE OLD HEAD BC REVERSEING THE LIST (a -> None | b -> c -> None)
            curr.next = headOfList
            
            # NOW CURR IS THE NEW HEAD OF THE LIST ( head: a -> None | hold: b -> c -> None
            headOfList = curr
            
            #make current node the next node we saved off
            # THE NEW HEAD IS THE SECOND NODE NOW ( head: a -> None | hold and CURRENT: b -> c -> None
            curr = hold; #

        return headOfList
        

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #list startsout empty
        newHead = None
        current = head
        
        while current:
            
            #first save the next pointer
            savedNextPtr = current.next

            # Make the pointer point to the head of the new list (basically replace newHead's status as head of our new list)
            current.next = newHead
            
            # Since we prepended a node to the newHead, the current node replaced it as the head, so update it as the new head
            newHead = current
            
            # The next node we need to reverse is the node we saved, bc that is the node that traditioanlly cam after the last node
            current = savedNextPtr
            
        return newHead

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

            
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:

        #each iteration, an element makes it's next node point to it, and then it makes itself point to nothing    
        def reverse(head):

            # BASE CASE WILL RETURN THE LAST NODE IN LIST
            if not head or not head.next: return head
            
            # recurse until we find the old tail, which will be the new head (fetch last node in list)
            newHead = reverse(head.next)
            
            #make our current node the new tail of the list and make the new head point to us. # make your OLD HEAD be the NEW TAIL (so a-> b -> None becomes b-> a -> None)
            head.next.next = head
            
            # The tail of a list always points to None
            head.next = None
            
            # Always return the new head of the list!
            # return the real head for the list (3) and next iteration will act on 1
            # this head never changes. THIS IS ALWAYS, ALWAYS, ALWAYS, THE LAST NODE IN YOUR ORIGINAL LIST.
            # IT NEVER CHANGES BC IT WILL ALWAYS, ALWAYS, ALWAYS, BE THE HEAD OF YOUR NEW LIST
            return newHead
        return reverse(head)Plonhe



class Solution5:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def reverse(head):
            
            # base case, return old tail
            if not head or not head.next: return head
            
            #Get tail of list
            tail = reverse(head.next)
            
            #make your next node point to yourself (reverse its ptr direction)
            head.next.next = head
            
            #Now that this node is the new tail, it needs to point to None
            head.next = None
            
            return tail
        
        return reverse(head)
        
            
    