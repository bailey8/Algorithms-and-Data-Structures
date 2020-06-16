 

class Solution4(object):
    def canJump(self, nums):

        #ENSURE THAT THE LIST IS NOT 1 ELEMENT OR EMPTY
        if not nums or len(nums) <= 1: True
     
        for i in range(0,range(len(nums)-1)):

            #If you are able to get to the last position from current spot, then update
            if nums[i] == 0: return False

            # SET THE NEXT CLEE TO THE "TRUE NUMBER OF HOPS WE HAVE"
            nums[i+1] = max(nums[i]-1,nums[i+1])

        return True


# BACKTRAKING
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        def backTrack(position):
            
            if position == len(nums)-1: return True
            
            # maxIndex = currentPos+available jumps or length of array
            furthestJump = min(len(nums)-1,nums[position]+position)
            
            # IF WE CAN'T REACH IT THEN BACKTRACK
            for i in range(position+1, furthestJump+1):
                if backTrack(i): return True
                
            return False
            
        return backTrack(0)
            
            
# BACKTRACKING with MEMO
class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = [0]*len(nums)
        #Mark last cell as valid, bc if we are at the last cell then we can reach the last cell
        memo[-1] = 1
        
        def canJumpFromPosition(position):
            
            # if we have the solution in the cache, then use it
            if memo[position] == 1: return True
            if memo[position] == -1: return False
            # If not, then find cells we can reach
            #If not, then calculate t
            furthestJump = min(position+nums[position],len(nums)-1)
            
            # set the cell to 1 if we can reach it
            for nextPosition in range(position+1,furthestJump+1):
                if canJumpFromPosition(nextPosition): 
                    memo[position] = 1
                    return True
                
            # set the cell to 0 if we cannot reach it
            memo[position] = -1
            return False
        
        return canJumpFromPosition(0)
            
            
        
 # BACKTRACKING
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = [0]*len(nums)
        #Mark last cell as valid, bc if we are at the last cell then we can reach the last cell
        memo[-1] = 1
        
        for position in reversed(range(len(nums)-1)):
            
            furthestJump = min(position+nums[position],len(nums)-1)
            
            # set the cell to 1 if we can reach it
            for nextPosition in range(position+1,furthestJump+1):
                if memo[nextPosition] == 1:
                    memo[position] = 1
                    break
                
           
        
        return memo[0] == 1
            
            
        
 
         


