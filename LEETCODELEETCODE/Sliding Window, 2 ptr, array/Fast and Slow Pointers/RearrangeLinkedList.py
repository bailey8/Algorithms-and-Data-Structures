class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def reverse(node):
            
            if not node or not node.next: return node
            
            tail = reverse(node.next)
            node.next.next = node    
            node.next = None
                        
            return tail
        
        def findMid(node):
            
            slow = fast = node
            
            while fast and fast.next:
                slow=  slow.next
                fast = fast.next.next
            
            #THIS WILL MAKE THE TAIL OF THE FIRST LIST POINT TO NONE - MODIFICATION
            middle = slow.next
            slow.next = None
            return middle
                
        if not head or not head.next: return head
        
        mid = findMid(head)
        list2 = reverse(mid)
        list1 = head
        
        while list1 and list2:
            
            temp = list1.next
            list1.next = list2
            list1 = temp
            
            temp = list2.next
            list2.next = list1
            list2 = temp
                     
 
