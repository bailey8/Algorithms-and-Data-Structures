# Add to the output all the intervals starting before newInterval.

# Add to the output newInterval.
# Merge it with the last added interval if newInterval starts before the last added interval.

# Add the next intervals one by one.
# Merge with the last added interval if the current interval starts before the last added interval.

# O(n) time, not in-place, make use of the 
# property that the intervals were initially sorted 
# according to their start times
def insert(self, intervals, newInterval):
    res, n = [], newInterval
    for index, i in enumerate(intervals):
        if i[-1] < n[0]:
            res.append(i)
        elif n[-1] < i[0]:
            res.append(n)
            return res+intervals[index:]  # can return earlier
        else:  # overlap case
            n[0] = min(n[0], i[0])
            n[-1] = max(n[-1], i[-1])
    res.append(n)
    return res