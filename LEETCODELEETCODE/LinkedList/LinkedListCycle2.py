class Solution(object):
    def detectCycle(self, head):
        visited = set()

        node = head
        
        while node is not None:
            
            #IF WE ARE SEEING THIS NODE AGAIN, THEN WE KNOW THERE IS A CYCLE
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None