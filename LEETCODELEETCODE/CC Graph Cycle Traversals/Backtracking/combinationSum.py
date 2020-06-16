class Solution:
    def combinationSum(self, candidates, target):
        
        # SORT THE NUMBERS
        candidates.sort()
        
        
        dp = [[[]]] + [[] for _ in range(target)]
        #[1,2,3] =  [ [ [] ] ,[],[],[]]
        
        for i in range(1, target + 1):
            
            # FOR EVERY NUMBER IS THE ARRAY
            for number in candidates:
                
                #IF THE NUMBER IS GREATER THAN THE TARGET, THEN BREAK CAUSE IT WILL EXCEED OUR TARGET SUM
                if number > i: break
                    
                #
                for L in dp[i - number]:
                    if not L or number >= L[-1]: dp[i] += L + [number],
        return dp[target]