class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            
            # store 3 in 1 -> 2 -> 3
            newHead = head.next
            
            # firstNode -> thirdNode
            head.next = head.next.next
            
            # secondNode -> firstNode -> thirdNode
            newHead.next = head
            
            # Make the second node's next equal to the swap of the next shit
            head.next = self.swapPairs(newHead.next.next) 
            # newHead.next.next = self.swapPairs(newHead.next.next)
            
            return newHead
        
        return head
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping - make last node of previous pair point to the correct swapped node of the next pair
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

sol = Solution()
head = sol.swapPairs(node)

while head:
    print(head.val, end = " ")
    head = head.next
