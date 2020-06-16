# Add to the output all the intervals starting before newInterval.

# Add to the output newInterval.
# Merge it with the last added interval if newInterval starts before the last added interval.

# Add the next intervals one by one.
# Merge with the last added interval if the current interval starts before the last added interval.

# O(n) time, not in-place, make use of the 
# property that the intervals were initially sorted 
# according to their start times
# class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        
        solution = []
        
        for index, i in enumerate(intervals):
            
            # IF THE INTERVAL ENDS BEFORE THE NEW INTERVAL STARTS, THEN ADD THE INTERVAL BC NO CONFLICT
            if i[-1] < newInterval[0]:
                solution.append(i)
                
            # IF OUR NEW INTERVAL ENDS BEFORE THE INTERVAL STARTS, THEN IT COMES BEFORE AND NO CONFLICTS
            elif newInterval[-1] < i[0]:
                
                # ADD THE NEW INTERVAL AND BE DONE WITH IT, BCTHE OTHERS ARE IN ORDER
                solution.append(newInterval)
                return solution+intervals[index:]  # can return earlier
            
            else:  # overlap case
                
                # THE NEW START TIME IS THE SMALLEST START TIME
                newInterval[0] = min(newInterval[0], i[0])
                
                #THE NEW END TIME IS THE LARGEST END TIME
                newInterval[-1] = max(newInterval[-1], i[-1])
        
        # THIS CASE ONLY GETS TRIGGERED IF THE NEW INTERVAL IS LAST BC WE WOULDNT HIT TERMINATION STATEMENT ABOVE
        solution.append(newInterval)
        return solution


class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        
        solution = []

        for index, interval in enumerate(intervals):
            start, end = interval
            newStart, newEnd = newInterval
            
            # IF THE INTERVAL ENDS BEFORE THE NEW INTERVAL STARTS, THEN ADD THE INTERVAL BC NO CONFLICT
            if end < newStart:
                solution.append(interval)
                
            # IF OUR NEW INTERVAL ENDS BEFORE THE INTERVAL STARTS, THEN IT COMES BEFORE AND NO CONFLICTS
            elif newEnd < start:
                
                # ADD THE NEW INTERVAL AND BE DONE WITH IT, BCTHE OTHERS ARE IN ORDER
                solution.append(newInterval)
                return solution+intervals[index:]  # can return earlier
            
            else:  # overlap case - DONT INSERT ANY INTERVALS HERE!!!! WE "CAPTURE!!!!!!!!!!!!" THE PREVIOUS INTERVAL, AND "ADD" TO THE ONE WE WANT TO INSERT
                
                # THE NEW START TIME IS THE SMALLEST START TIME
                newInterval[0] = min(newStart, start)
                
                #THE NEW END TIME IS THE LARGEST END TIME
                newInterval[-1] = max(newEnd, end)
        
        # THIS CASE ONLY GETS TRIGGERED IF THE NEW INTERVAL IS LAST BC WE WOULDNT HIT TERMINATION STATEMENT ABOVE
        solution.append(newInterval)
        return solution


