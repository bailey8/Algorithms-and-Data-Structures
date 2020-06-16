def eraseOverlapIntervals(self, intervals):        
     if not intervals == 0:
        return 0
        intervals.sort(intervals, lambda x: x[0])
        dp = []* len(intervals)
        dp[0] = 1
        ans = 1
        for i in range(len(intervals)):
            big = 0
            for j in range(end,-1,-1):
                if intervals[j][-1] > intervals[i][0]:
                    big = max(dp[j], big)
            dp[i] = big + 1
            ans = max(ans, dp[i])
        return len(intervals) - 
        

# 56 Merge Intervals <- very similar, i did it with just 3 lines different
# 252 Meeting Rooms
# 253 Meeting Rooms II
# 452 Minimum Number of Arrows to Burst Balloons

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        start,end = 0, -1
        intervals.sort(key = lambda x: x[0])
        count = 0
        for prev in range(len(intervals)-1):
            cur = prev+1
            # Overlapping interval
            if intervals[cur][start] < intervals[prev][end]:
                # Shrink the current interval so that its ending is the smallest of the two conflicts
                # This way, you will be minimizing the space the thing takes up
                intervals[cur][end] = min(intervals[prev][end], intervals[cur][end])
                count += 1
        return count

def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        intervals.sort(key=lambda x: x.start)  # sort on start time
        currEnd, cnt = intervals[0].end, 0
        for x in intervals[1:]:
            if x.start < currEnd:  # find overlapping interval
                cnt += 1
                currEnd = min(currEnd, x.end)  # erase the one with larger end time
            else:
                currEnd = x.end   # update end time
        return cnt