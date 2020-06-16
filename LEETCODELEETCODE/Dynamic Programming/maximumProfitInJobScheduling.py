class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        def findPrevProfit(jobIndexPassedIn):
            
            # WE NEED TO FIND THE FIRST JOB THAT ENDS BEFORE THIS JOB STARTS
            startTime =start[jobIndexPassedIn]

            # CYCLE BACKWARDS UNTIL WE FIND A NON-CONFLICTING JOB
            for previousNonConflictingJob in reversed(range(jobIndexPassedIn)):
                # IF THE JOBS DO NOT CONFLICT
                if end[previousNonConflictingJob] <= startTime:
                    #RETURN TOTAL PROFIT OF FIRST NON-CONFLICTING JOB
                    return memo[previousNonConflictingJob]

            # IF ALL JOBS CONFLICT THEN RETURN 0
            return 0
        
        jobs = zip(startTime,endTime,profit) # [ (start, end, profit) ....]
        
        # SORT JOBS BY END TIME
        jobs = sorted(jobs,key = lambda x: x[1])
        # UNPACK INTO TUPLES
        start, end, profit = zip(*jobs) # back to normal, but now all orders are based off sorted order
        
        # WE TRACK THE MAXIMIM VALUE AT EVERY MEETING TIME
        memo = list(profit)
 
        for jobNumber in range(1,len(endTime)):
            
            # EITHER include the current job and the last profit you could make from last non conflicting job
            # OR skip the current job and use the last job
            memo[jobNumber] = max(memo[jobNumber] + findPrevProfit(jobNumber), memo[jobNumber-1])

        return memo[-1]