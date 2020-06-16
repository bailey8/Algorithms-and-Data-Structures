class Solution:    
    def eraseOverlapIntervals(self,intervals):
    
        #SIMILIAR TO LONGEST INCREASING SUBSEQUENCE
        def erase_Overlap_Intervals(prev, curr, intervals):

            if curr == len(intervals): return 0
            taken = nottaken = float('inf')
            
            
            #-----EACH RECURSION TRY 2 THINGS -------------------------#
            #  1) KEEP CURRENT ELEMENT (IF IT IS VALID TO DO SO - IT MAY NOT ALWAYS BE VALID ("COULD START TOO SOON"))
            #  2) DON'T INCLUDE CURRENT ELEMENT, AND KEEP THE LAST ELEMENT AS YOUR "PREVIOUS" ELEMENT/INTERVAL FOR COMPARISON PURPOSES
            # IN FUTURE ITERATIONS - THE PREVIOUS ELEMENTS END TIME WILL "STILL" BE USED FOR COMPARISON AS THE "PREV" EVEN THOUGH IT WAS A 
            #COUPLE "PREVS" BACK

            # IF THE PREVIOUS INTERVAL ENDS BEFORE THIS ONE STARTS, THEN WE DONT NEED TO DELETE IT
            if prev == -1 or intervals[prev][-1] <= intervals[curr][0]:
                #THE NEXT "PREVIOUS" WILL BE THIS CURRENT INTERVAL (THATS WHY WE PASS "CURR" IN), BECAUSE WE ARE USING IT
                taken = erase_Overlap_Intervals(curr, curr + 1, intervals)
            
            # WE ARE NOT USING THIS INTERVAL, SO THE PREVIOUS INTERVAL WILL STAY THE SAME
            # ITS NOT CURR BECAUSE THAT WOULD IMPLY WE ARE USING THE CURRENT INTERVAL ----- THAT MEANS WE WOULD DELETE ONE
            # WE ADD ONE HERE, BECAUSE THIS MEANS WE ARE "SKIPPING" AN INTERVAL, WHICH MEANS WE ARE NOT USING IT, OR DELETING IT
            nottaken = erase_Overlap_Intervals(prev, curr + 1, intervals) + 1

            #TAKE WHICHEVER OPTION MAKES YOU DELETE THE FEWEST INTERVALS
            return min(taken, nottaken)

        # SORT OFF THE START TIME OF THE INTERVALS
        intervals.sort(key = lambda x: x[0])
        return erase_Overlap_Intervals(-1, 0, intervals)
    

class Solution:
     
    def eraseOverlapIntervals(self,intervals):
        if len(intervals)== 0:
            return 0

        # SORT INTERVALS BY END TIME
        intervals.sort(key = lambda x: x[1])

        # OUR "PREVIOUS" INTERVAL IS THE FIRST INTERVAL
        prev = count = 0
       
        for i in range(1,len(intervals)):

            #DELETE THE INTERVAL IF IT CONFLICTS
            if intervals[prev][-1] > intervals[i][0]:
                count += 1
            # IF NO CONFLICT THEN MARK THE INTERVAL AS VALID AND MAKE IT THE NEW PREVIOUS INTERVAL
            else: prev = i
            
        
        return count
 