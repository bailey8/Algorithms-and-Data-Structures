class Solution:
    def numDecodings(self,s):

        def helper(ptr):
            
            if ptr >= len(s): return 1
            
            if cache[ptr] > -1: return cache[ptr]
            
            total = 0
            for i in range(1,3):
                if ptr + i <= len(s):
                    snippet = s[ptr:ptr+i]
                    if valid(snippet):
                        total += helper(ptr+i)
            
            cache[ptr] = total
            return cache[ptr]
                        
        
        def valid(string):
            
            if len(string) == 0 or string[0] == '0':
                return False
            
            return 1 <= int(string) <= 26
        
        cache = [-1] *len(s) 
        return helper(0)

print(Solution().numDecodings("10"))



class Solution:
    def numDecodings(self, s: str) -> int:
        
        # This must be 1 extra index
        cache = [1]* (len(s)+1)
        
        for i in reversed(range(len(s))):
            
            # WE CANNOT MAKE ANY DECODES BEAUSE THE DECODE CANNOT START WITH 0
            if s[i] == '0': cache[i] = 0
                
            # ONLY DO THIS IF WE HAVE THE ABILITY TO SEARCH i+2 to the right
            # We an handle len(n)-2 bc the cache is 1 extra element long, so we really only need to skip 1 element
            elif i < len(s)-1:
                
                # WE CAN ALWAYS APPEND K+1 TO K+2 AND THEN NOT MAKE ANY CHOICES
                cache[i] = cache[i+1]

                # WE CAN APPEND K TO K+1, AND THEN ADD THE DECODES AT K+2 BC WE DON'T HAVE TO 
                # WORRY ABOUT K+1 BEING APPENDED TO K+2 BC WE MADE THE CHOICE TO APPEND K+1 TO K
                if s[i] == '1' or (s[i] == '2' and s[i+1] < '7'): cache[i] += cache[i+2]
                    
        return cache[0]

     
        

        
class Solution:
    def numDecodings(self,s):
        if len(s) == 0 or s[0] == '0': return 0
        # r2: decode ways of s[i-2] , r1: decode ways of s[i-1] 
        current = prev = 1
        
        for i in range(1,len(s)):
            # zero voids ways of the last because zero cannot be used separately
            if s[i] == '0': current = 0

            # possible two-digit letter, so new r1 is sum of both while new r2 is the old r1
            if s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
                
                #we say, "okay, I will wither "
                current,prev = prev + current, current
             

            #
            else: prev = current 

        return current