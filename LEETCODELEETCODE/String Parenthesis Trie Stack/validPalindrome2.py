class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(left,right):
            while left < right:
                if s[left] != s[right]: return False
                left += 1
                right -=1
            return True
        
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] != s[right]: return helper(left+1,right) or helper(left,right-1)
            left +=1
            right -=1
    
        return True
            
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        
        
        def recursion(left,right,count = 0):
            
            if left >= right: return True
            
            if count == 0 and s[left] != s[right]:
                return recursion(left+1,right, 1) or recursion(left,right-1, 1)
            
            if s[left] == s[right]: return recursion(left+1, right-1, count)
            
            return False
            
            
        return recursion(left,right)
            