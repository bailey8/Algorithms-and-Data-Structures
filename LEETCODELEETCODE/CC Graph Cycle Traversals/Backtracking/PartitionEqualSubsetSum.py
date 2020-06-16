

# BACKTRACKING SOLUTION
import collections
class Solution(object):
    def canPartition(self, nums):
        
        def canFindSum(target, ind):

            if target in cache: return cache[target]
            # BASE CASES
            if target == 0: return True
            if target < 0 or ind == len(nums): return False
            
            # EITHER USE OR DO NOT USE THE REMAINING NUMBERS. THIS IS WHAT THE FOR LOOP DOES!!!
            
            cache[target] = canFindSum(target - nums[ind], ind+1) or canFindSum(target, ind+1)

            return cache[target]

        cache = collections.defaultdict(bool)
        s = sum(nums)

        # IF THE TARGET SUM IS A FRACTION - FORGET IT
        if s % 2 != 0: return False

        # SEARCH FOR A SUBSET SUM THAT REACHES OUR TARGET. IF WE FIND ONE, THEN WE KNOW THE OTHER EXISTS!!!
        return canFindSum(s/2, 0)


# with VALUE array O(N^2) space
class Solution(object):
    
    def canPartition(self, nums):
        
        s = sum(nums)

        # IF THE TARGET SUM IS A FRACTION - FORGET IT
        if s % 2 != 0 or len(nums) < 2: return False
        
        target = int(s/2)
        
        cache = [[0 for _ in range(target+1)] for _ in range(len(nums)+1)]
            
        for row in range(1,len(cache)):
            for col in range(1,len(cache[0])):
                
                # IF THE AMOUNT IS LESS THAN THE NUMBER, THEN WE CANT USE THE NUMBER, SO DEFUALT TO CELL ABOVE
                if nums[row-1] <= col:
                    cache[row][col] = max(cache[row-1][col-nums[row-1]] + nums[row-1], cache[row-1][col])
                else: cache[row][col] = cache[row-1][col]
                    
        return True if cache[-1][-1] == target else False
 
 

# BACKTRACKING SOLUTION
import collections
class Solution(object):
    def canPartition(self, nums):
        
        total = sum(nums)
        if total % 2 != 0 or len(nums) < 2: return False
        target = int(total/2)
        
        #cache must hold each amount and each number. amount should be columns
        cache = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        
        # Always able to make a subset of 0 regardless of numbers
        for row in cache:
            row[0] = True
            
        for row in range(1,len(cache)):
            for col in range(1,len(cache[0])):
                
                index = row-1
                
                # IF WE CAN MAKE THIS SUM WITH OR WITHOUT USING THE CURRENT NUMBER, THEN MARK IT AS SO
                if nums[index] <= col: cache[row][col] = cache[row-1][col] or cache[row-1][col-nums[index]]
                
                #IF WE CANT SUBTRACT THE NUMBER BC ITS GREATER THAN THE COLUMN WE ARE IN, THEN MAKE SUM WITHOUT THE NUMBER
                else: cache[row][col] = cache[row-1][col]
                    
        return cache[-1][-1]   
    

# O(target) space
 class Solution(object):
    
    def canPartition(self, nums):
        
        s = sum(nums)

        # IF THE TARGET SUM IS A FRACTION - FORGET IT
        if s % 2 != 0 or len(nums) < 2: return False
        
        target = int(s/2)
        
        cache = [False for _ in range(target+1)]
        cache[0] = True
            
        for num in nums:
            for col in range(target,0,-1):
                
                # IF THE AMOUNT IS LESS THAN THE NUMBER, THEN WE CANT USE THE NUMBER, SO DEFUALT TO CELL ABOVE
                if col >= num:
                    cache[col] =  cache[col-num] or cache[col]
                    
                else: cache[col] = cache[col]
                    
        return cache[-1]
         
                
                
 
         
                
 