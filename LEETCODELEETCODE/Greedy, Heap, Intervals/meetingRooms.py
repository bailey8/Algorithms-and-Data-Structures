class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key = lambda x: x[0])
        
        #sort by start time, and if there is 1 conflict then return
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][-1]: return False
            
        return True
        