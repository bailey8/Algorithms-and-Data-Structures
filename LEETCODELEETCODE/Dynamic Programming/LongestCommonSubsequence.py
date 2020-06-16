class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # COMPARING AN EMPTY STRING HAS 0 IN COMMON
        cache = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        
        # FOR EVERY COMBINATION OF CHARACTER PAIRS
        for i in range(1,len(text2)):
            for j in range(1,len(text1)):
                # IF THE CHARACTERS MATCH, THEN ADD 1 TO RESULT AND SHAVE OFF MATCHING CHARACTER
                if text2[i-1] == text1[j-1]: cache[i][j] = 1 + cache[i-1][j-1]
                #IF NOT, THEN TRY TO SHAVE OFF 1 CHRACTER ON EACH SIDE. KEEP THE GREATEST RESULT
                else: cache[i][j] = max(cache[i-1][j],cache[i][j-1])
        
        return cache[-1][-1]
                
        


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def rec(left,right):
            
            if left == -1 or right == -1: return 0
            if cache[left][right] > -1: return cache[left][right]
            
            if text1[left] == text2[right]: cache[left][right] = 1 + rec(left-1,right-1)
            else: cache[left][right] =  max(rec(left-1,right),rec(left,right-1))
            return cache[left][right]
        
        return rec(len(text1)-1,len(text2)-1)
                
        
print(0 == True)
