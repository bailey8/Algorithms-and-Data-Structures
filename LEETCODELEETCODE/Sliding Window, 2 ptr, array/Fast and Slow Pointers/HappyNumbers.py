class Solution:
    def isHappy(self, n: int) -> bool:
        
        def square(n):
            
            total = 0
            while n != 0:
                total += (n % 10) ** 2
                n //= 10
                
            return total
                
        
        slow, fast = square(n), square(square(n))
        
        if fast == 1: return True
        
        # Stop once there is a cycle
        while slow != fast:
            
            slow = square(slow)
            fast = square(square(fast))
            if fast == 1: return True
            
        return False
    
        
            
            