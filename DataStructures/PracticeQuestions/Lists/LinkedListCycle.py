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
class Solution(object):
    def hasCycle(self,head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
            if slow is fast:
                return True
        return False