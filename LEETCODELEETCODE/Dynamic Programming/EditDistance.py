class Solution:
    def  minDistance(self, s1, s2):
        
        def levenshteinDistance(s1Index , s2Index):
            
            #DELETE ALL CHARACTERS IN S2 IF S1 IS EMPTY STRING
            if s1Index < 0:
                return s2Index + 1 # If s1 is "", it is all insertions to get s1 to s2
            # DELETE ALL CHARACTERS IN S1 IF S2 IS THE EMPTY STRING
            elif s2Index < 0:
                return s1Index + 1 # If s2 is "", it is all deletions to get s1 to s2

            # RETURN THE CACHED RESULT IF IT IS THERE
            if cache[s1Index][s2Index] != -1: return cache[s1Index][s2Index]

            #Characters match - no repair needs to take place, no addition to distance
            if s1[s1Index] == s2[s2Index]: cache[s1Index][s2Index] = levenshteinDistance(s1Index - 1, s2Index - 1)

            else:
                
                deleteFromS1 = levenshteinDistance(s1Index - 1, s2Index)
                deleteFromS2 = levenshteinDistance(s1Index, s2Index - 1)
                replace = levenshteinDistance(s1Index - 1, s2Index - 1)

                #   We want to take the minimum of these 3 options to fix the problem (we add 1 to the min cost action to symbolize performing the operation)
                cache[s1Index][s2Index] = 1 + min(deleteFromS1 , deleteFromS2, replace)
            
            return cache[s1Index][s2Index]

        
        cache = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
        return levenshteinDistance(len(s1) - 1,len(s2) - 1)



class Solution:
    def  minDistance(self, s1, s2):
        
        if not s1 and not s2: return 0
        
        opt = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        
        # INITIALIZE THE FIRST ROW AND FIRST COLUMN OF THE CACHE
        for row in range(len(s1)+1): opt[row][0] = row
        for col in range(len(s2)+1): opt[0][col] = col
            
        # FOR EVERY CELL IN THE CACHE
        for row in range(1,len(s1)+1):
            for col in range(1,len(s2)+1):
                
                # IF THE CHARACTERS MATCH, THEN DELETE THEM BOTH BC NO EDIT DISTANCE NEEDED
                if s1[row-1] == s2[col-1]: opt[row][col] = opt[row-1][col-1]
                    
                # TAKE THE MINIMUM OF REPLACEMENT, DELETE FROM S1, OR DELETE FROM S2
                else: opt[row][col] = 1 + min(opt[row-1][col-1],opt[row][col-1],opt[row-1][col])
                    
        return opt[-1][-1]



