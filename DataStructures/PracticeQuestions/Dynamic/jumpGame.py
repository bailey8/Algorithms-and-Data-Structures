# Naive Recursive

# class Solution(object):
#     def canJump(self, nums):
#         return self.help(nums,0)
    
#     def help(self,nums,index):
#         if index == len(nums)-1:
#             return True
#         if nums[index] == 0: return False
#         for i in range(1,nums[index] +1):
#             good = self.help(nums,i+index)
#             if good == True:
#                 return True
#         return False

class Solution(object):
    memo = []
    def canJump(self, nums):
        self.memo = [0]*len(nums)
        self.memo[-1] = 1
        return self.help(nums,0)
    
    def help(self,nums,index):
        if nums[index] == 0: self.memo[index] = -1
        if self.memo[index] !=0:
            return self.memo[index] == 1
        for i in range(1,nums[index] +1):
            good = self.help(nums,i+index)
            if good == True:
                self.memo[i+index] == 1
                return True
        self.memo[i+index] = -1
        return False

# Proper memoization
# class Solution(object):
#     memo = []
#     def canJump(self, nums):
#         self.memo = [0]*len(nums)
#         self.memo[-1] = 1
#         return self.help(nums,0)
    
#     def help(self,nums,position):
#         if self.memo[position] !=0:
#             return self.memo[position] == 1
#         furthestJump = min(position + nums[position], len(nums) - 1);
#         for nextPosition in range(position+1,furthestJump +1):
#             if self.help(nums,nextPosition):
#                 self.memo[position] == 1
#                 return True
#         self.memo[position] = -1
#         return False

class Solution2(object):
    def canJump(self, nums):
        memo = [0]*(len(nums))
        memo[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            nextposition = min(len(nums)-1,nums[i] + i)
            for j in range(i+1,nextposition+1):
                # If the next position is good, and we can get there from current position, we then know our current position is also good
                if memo[j] == 1:
                    memo[i] = 1
                    break
        return memo[0] == 1

class Solution3(object):
    def canJump(self, nums):
        lastposition = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            #If you are able to get to the last position from current spot, then update
            if i + nums[i] >= lastposition:
                lastposition = i
        return lastposition == 0




