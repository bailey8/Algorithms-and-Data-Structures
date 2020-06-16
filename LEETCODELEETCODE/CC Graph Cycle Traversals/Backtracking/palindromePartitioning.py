class Solution:
    def partition(self, s: str):
        
        def isPalindrome(string):
            left, right = 0, len(string)-1
            
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -=1

            return True
        
        def search(index = 0,path = []):
            
            if index == len(s): 
                palindromes.append(path)
                return
            
            for i in range(index, len(s)):
                substring = s[index:i+1]
                if isPalindrome(substring): search(i+1, path + [substring])
            
            return
            
        palindromes= []
        search()
        return palindromes

print(Solution().partition("aac"))