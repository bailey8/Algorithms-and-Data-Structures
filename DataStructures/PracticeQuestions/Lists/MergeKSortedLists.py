from queue import PriorityQueue
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time complexity : O(Nlogk) where k is the number of linked lists.

# The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
# There are N nodes in the final linked list.
# Space complexity :

# O(n) Creating a new linked list costs O(n)O(n) space.
# O(k) The code above present applies in-place method which cost O(1)O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations). 


class Solution(object):
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        queue =PriorityQueue()
        for l in lists:
            if l:
                queue.put((l.val,l))
        while not queue.empty():
            val, node = queue.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                queue.put((node.val, node))
        return head.next
     

[[1,4,5],[1,3,4],[2,6]]

node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(5)
node2 = ListNode(2)
node2.next = ListNode(3)
node2.next.next =ListNode(4)
node3 = ListNode(3)
node3.next = ListNode(6)

obj = Solution()
print(obj.mergeKLists([node1,node2,node3]))



        


