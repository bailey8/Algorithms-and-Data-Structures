
class Solution2:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
        return merged


a# CONSTANT SPACE
class Solution:
    def merge(self, intervals):
        intervals.sort( key = lambda x: x[0])

        indexOfLastMerged = 0
        for i in range(1, len(intervals)):

            # IF THE LAST INTERVAL ENDS AFTER THIS ONE STARTS THEN UPDATE THE END OF IT
            if intervals[indexOfLastMerged][1] >= intervals[i][0]:
                intervals[indexOfLastMerged][1] = max(intervals[indexOfLastMerged][1], intervals[i][1])
            
            # IF THE LAST INTERVAL STARTS AFTER THE LAST INTERVAL ENDS, THEN JUST UPDATE THE INDEX OF THE LAST INTERVAL
            else:
                indexOfLastMerged += 1
                intervals[indexOfLastMerged] = intervals[i]
                
        return intervals[:indexOfLastMerged + 1]