
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

# Bottom up again - SET THE 0 INDEX AS 1 - WIERD IKKKKK
def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [0]*n
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]

# Bottom up, constant space
def climbStairs3(self, n):
    if n == 1: return 1
    level1,level2  = 1, 2
    for i in range(2, n):
        # Set the new 'i-1' equal to the previous 'i-2' cause we are incrementing
        level1,level2 = level2, level1+level2
    return level2

# Top down + memorization (list)
def climbStairs4(self, n):
    if n == 1:
        return 1
    dic = [-1 for i in range(n)]
    dic[0], dic[1] = 1, 2
    return self.helper(n-1, dic)
    
def helper(self, n, dic):
    if dic[n] < 0:
        dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
    return dic[n]
    
# Top down + memorization (dictionary)  
def __init__(self):
    self.dic = {1:1, 2:2}
    
def climbStairs(self, n):
    if n not in self.dic:
        self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    return self.dic[n]