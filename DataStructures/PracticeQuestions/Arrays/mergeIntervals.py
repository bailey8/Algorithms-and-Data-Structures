def merge(intervals):
    size = len(intervals)
    for row in range(0,size-1):
        if intervals[row][-1] >= intervals[row+1][-1] or intervals[row][-1] >= intervals[row+1][0]:
            intervals[row+1] = [intervals[row][0],intervals[row+1][-1]]
            intervals.pop(row)
            row -=1
            size -=1
           
    return intervals
  
  
print(merge([[2,2],[3,3],[5,7],[2,2],[4,6]]))
 #Stops at 4th index
 