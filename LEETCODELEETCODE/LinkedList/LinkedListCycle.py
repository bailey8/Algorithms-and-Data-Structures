class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Method1 - Hashtable
def hasCycle(head):
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False

 
# Two pointer

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow_ptr = fast_ptr = head
        
        # ENSURE THAT FAST_PTR HAS A VALID NEXT ELEMENT
        # CHECK FAST_PTR FIRST TO SHORT CIRCUIT THE BOOLEAN
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            
            # IF THEY EQUAL THEN WE FOUND A CYCLE
            if fast_ptr is slow_ptr: return True
            
        return False

        