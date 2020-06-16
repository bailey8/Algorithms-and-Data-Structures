 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        def __lt__(self, other):
            return self.val < other.val

class Solution(object):
    def mergeKLists(self, lists):
        if not lists: return 
        
        #JUST RETURN THE SINGLE LIST IF THERES ONLY 1 - BASE CASE! BASE CASE! BASE CASE!
        if len(lists) == 1: return lists[0]
        
        # NO SPACE COMPLEXITY HERE BC SHALLOW COPY
        mid = len(lists)//2

        # I NEED TO CAPTUEE THE LEFT AND RIGHT BC THE RECURSIVE FUNCITON RETURNS LISTS
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        
        # ONCE WE GET TWO LISTS, MERGE THEM
        return self.merge(l, r)

    # O(1) SPACE BECEAUSE WE ARE JUST USING EXISTING NODES
    def merge(self, leftList, rightList):
        
        # WE NEED THIS DUMMY VARIABLE TO APPEND OUR FIRST VALUE TO
        dummy = current = ListNode(0)
        while leftList and rightList:
            if leftList.val < rightList.val:
                current.next = leftList
                leftList = leftList.next
            else:
                current.next = rightList
                rightList = rightList.next
            current = current.next
            
        # IF THERE ARE STILL MORE ELEMENTS IN EITHER LIST, THEN JUST APPEND "ALL" REMAINING
        #TO THE END OF THE LIST
        if not leftList: current.next=rightList
        else: current.next=leftList
            
        # WE ADDED OUR "FIRST" ELEMENT TO HEAD.NEXT, SO THAT IS WHERE THE LIST STARTS
        return dummy.next


import heapq
class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        heap = []
        
        # ADD ALL THE LINKED LISTS TO PRIORITYQUEUE
        #SORT OFF THE VALUE OF THE HEADS OF THE LINKEDLISTS
        for linkedList in lists:
            if linkedList:
                # THIS SORTS OFF THE VALUE OF THE FIRST ITEM IN TUPLE
               heapq.heappush(heap,(linkedList.val, linkedList))
                
        #WHILE WE STILL HAVE AN ELEMENT IN THE PQUEUE
        while heap:
            #POP THE SMALLEST ITEM FROM THE QUEUE
            val, node = heapq.heappop(heap)
            
            #APPEND THIS VALUE TO OUR LINKEDLIST
            point.next = ListNode(val)
            # UPDATE OUR POINTER TO POINT TO THIS NEW VALUE
            point = point.next
            
            # NOW INCREMENT THE LINKEDLIST WE POPPED, BC WE USED A NODE FROM IT
            node = node.next
            # IF THERE ARE STILL MORE ELEMENTS IN THE LINKEDLIST THEN PUSH IT BACK TO THE QUEUE
            if node:
                heapq.heappush(heap,(node.val, node))
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

obj = Solution2()
head = obj.mergeKLists([node1,node2,node3])
while head:
    print(head.val, end = " ")
    head = head.next

        


import heapq

heap = []
node1 = ListNode(5)
node2 = ListNode(10)
heapq.heappush(heap,(node1.val,node1))
heapq.heappush(heap,(node2.val,node2))
val,node = heapq.heappop(heap)
print(val,node.val)

