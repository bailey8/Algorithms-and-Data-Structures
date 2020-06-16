class Solution:

    def isPalindrome(self, head) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        middleNode = self.findMiddle(head)
        list2 = self.reverse_list(middleNode.next)

        # Check whether or not there's a palindrome.
        result = True
        list1 = head
        while result and list2:
            if list1.val != list2.val: return False
            list1 = list1.next
            list2 = list2.next

        # Restore the list and return the result.
        middleNode.next = self.reverse_list(list2)
        return True    

    def findMiddle(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        def reverse(node):
            
            if not node or not node.next: return node
            
            tail = reverse(node.next)
            
            node.next.next = node     
            node.next = None
            
            return tail
        
        
        def findMid(node):
            
            fast = slow = node
            
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            
            return slow
        
        if not head or not head.next: return True
        
        list2 = reverse(findMid(head))
        list1 = head
        
        while list2 and list1:
            
            if list1.val != list2.val: return False
            list1 = list1.next
            list2 = list2.next
            
        return True
            
            
        
        