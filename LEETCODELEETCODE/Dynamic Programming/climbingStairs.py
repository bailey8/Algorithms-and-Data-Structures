
# brute force O(2^n)
class Solution(object):
    def climbStairs(self, n):
        return self.helper(n,0)
    def helper(self,n,count):
        if count == n:
            return 1
        if count > n:
            return 0
        return  self.helper(n,count+1) + self.helper(n,count+2)

# Memo bottom up
class SolutionBottomUp(object):
    def climbStairs(self, n):
        return self.helper(n,0,{})
    
    def helper(self,n,count,memo):
        if count == n: return 1
        if count > n: return 0
        if count+1 not in memo: memo[count+1] = self.helper(n,count+1,memo)
        if count+2 not in memo: memo[count+2] = self.helper(n,count+2,memo)
        
        return memo[count+1] + memo[count+2]

# Memo top down
class SolutionTopDown(object):
    def climbStairs(self, n):
        return self.helper(n,{})
    
    def helper(self,count,memo):
        if count == 0: return 1
        if count < 0: return 0
        if count-1 not in memo: memo[count-1] = self.helper(count-1,memo)
        if count-2 not in memo: memo[count-2] = self.helper(count-2,memo)
        
        return memo[count-1] + memo[count-2]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        
        dp = [0]*(n+1)
        
        # 1 WAY TO GET TO FIRST STEP
        dp[1] = 1
        # 2 WAYS TO GET TO SECOND STEP
        dp[2] = 2
        
        # WE CAN REACH THIS STEP FROM EITHER OF THE 2 PREVIOUS STEPS
        # SO ADD THE WAYS TO GET TO THOSE TO THIS STEP
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        # THE FINAL STEP WILL BE THE ANSWER
        return dp[-1]
       
            

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Bottom up, constant space
        if n == 1: return 1

        # THE FIRST TWO LEVELS HAVE THIS AMOUNT OF WAYS TO GET TO
        level1, level2  = 1, 2

        #STARTING ON THE THIRD STAIR
        for i in range(3, n+1):
            # THE NEW LEVEL 1 IS THE OLD LEVEL 2 AND THE NEW LEVEL 2 IS THE SUM OF PREVIOUS REACHABLE LEVELS
            level1,level2 = level2, level1+level2
        return level2


 
            
                


# Top down + memorization (dictionary)  
def __init__(self):
    self.dic = {1:1, 2:2}
    
def climbStairs(self, n):
    if n not in self.dic:
        self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    return self.dic[n]