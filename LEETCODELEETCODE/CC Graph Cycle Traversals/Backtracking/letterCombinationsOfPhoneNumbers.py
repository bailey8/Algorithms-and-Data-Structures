class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans = []
        def dfs(index,path):
            
            # BASE CASE, WE HAVE EXPLORED ALL THE NUMBERS
            if index == len(digits): 
                ans.append(path)
                return
            
            # create a new branch for letter we could take
            for letter in phone[digits[index]]:
                dfs(index+1,path + letter)
                
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        if digits: dfs(0,"")
        return ans
            
            
                
            
            