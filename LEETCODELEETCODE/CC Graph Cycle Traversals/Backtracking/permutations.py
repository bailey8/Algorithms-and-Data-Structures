



# TO ACCOUNT FOR DUPLICATES
class Solution:
    def permuteUnique(self,nums):
      
        def dfs(used,array):

            if len(array)==len(nums):
                res.append(array.copy())
                return
            
            for i in range(len(nums)):
                if used[i]: continue
                    
                # WE DONT NEED TO SWAP THE DUPLICATE CHARACTER IN!
                if i>0 and nums[i-1]==nums[i] and not used[i-1]: continue
                used[i] = True
                array.append(nums[i])
                dfs(used,array)
                used[i]= False
                array.pop()

        res = []
        if not nums or len(nums) == 0: return res
        used = [False] * len(nums)
        array = []
        nums.sort()
        dfs(used, array)
        return res



class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        used = [False] * len(nums)
        answer = []
        
        def backtrack(path):
            
            if len(path) == len(nums): answer.append(path.copy())
            for index, num in enumerate(nums):
                if not used[index]: 
                    used[index] = True; path.append(num)
                    backtrack(path)
                    path.pop(); used[index] = False
                
        backtrack([])
        return answer
            
         