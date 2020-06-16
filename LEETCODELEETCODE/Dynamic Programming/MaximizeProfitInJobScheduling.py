 
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = zip(startTime,endTime,profit)
        jobs = sorted(jobs,key = lambda x: x[1])
        start, end, profit = zip(*jobs)
        memo = [value for value in profit]
 
        for i in range(1,len(endTime)):
            memo[i] = max(memo[i] + self.findPrevProfit(i,end,start,memo), memo[i-1])
        return memo[-1]


    def findPrevProfit(self,startIndex,endTimes,startTimes,memo):
        index = startIndex -1
        startTime =startTimes[startIndex]
        while index >= 0:
            if endTimes[index] <= startTime:
                return memo[index]
            index -= 1
        return 0

 
class Solution2(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = zip(startTime,endTime,profit)
        jobs = sorted(jobs,key = lambda x: x[1])
        start, end, profit = zip(*jobs)
        memo = [value for value in profit]
        if i < 0 
        return memo[-1]


    def findPrevProfit(self,startIndex,endTimes,startTimes,memo):
        index = startIndex -1
        startTime =startTimes[startIndex]
        while index >= 0:
            if endTimes[index] <= startTime:
                return memo[index]
            index -= 1
        return 0


sol = Solution()
print(sol.jobScheduling([1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60]))

        
            

 