import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        
        #sort meetings by start time
        intervals.sort(key = lambda x: x[0])
        
        #hold number of available meeting rooms
        maximum = 0
        inUse = 0
        heap = []
        
        for start, end in intervals:
            
            #If this meeting starts before the earliest meeting ends, then we need a new
            # room bc they are all conflicting (if the earliest meeting conflicts then they all will)
            if not heap or start < heap[0]:
                
                #add the end time to the heap bc we are only concerned with the end for comparison purposes
                heapq.heappush(heap,end)
                # now that we added a room, increment inUse to show we have 1 more active room
                inUse += 1
                #This tracks the maximum number of rooms we have needed for all meetings
                maximum = max(maximum,inUse)
            
            else:
                # if the meetings start time is after the end time of the active meetings
                # Then that means that meeting will end before this new one starts so discard it
                while heap and start >= heap[0]:
                    heapq.heappop(heap)
                    inUse -=1
                
                # after removing all the meetings that end before this one starts, push the meeting on the heap
                heapq.heappush(heap,end)
                inUse += 1
                    
        return maximum
        
        
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        #sort meetings by start time
        intervals.sort(key = lambda x: x[0])
        
        #hold number of available meeting rooms
        maximum = 0
        in_use = 0
        
        heap = []
        
        for start,end in intervals:
            
            # If the earlies meeting ends after yours starts, you must claim a new room
            if not heap or start < heap[0]:
                heapq.heappush(heap,end)
                
            else:
                #wait for all the meetings that end before you to finish
                while heap and start >= heap[0]: 
                    heapq.heappop(heap)
                    in_use -= 1
                # start your meeting after the others have finsihed
                heapq.heappush(heap,end)
                
            in_use += 1
            maximum = max(in_use,maximum)
        
        return maximum
