

def minimize(intervals):

    # [[deadline,duration], [deadline,duration]]
    # SORT BY DEADLINES
    intervals.sort(key = lambda x: x[0])
    delay = 0
    schedule = []
    time = 0
 
    for i in range(len(intervals)):
        start = time
        end = start + intervals[i][1]
        schedule.append([start,end])
        time = end
        delay += max(0,end-intervals[i][0])

    return (schedule,delay)

meetings = [ [900,5],[99999,5000],[2,1],[9999,5000]]
print(minimize(meetings))

