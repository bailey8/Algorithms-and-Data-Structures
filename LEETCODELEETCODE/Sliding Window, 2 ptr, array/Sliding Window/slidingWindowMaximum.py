from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
 
        if not nums: return []
        if k == 0: return nums

        # Defining Deque and result list
        largestElements = deque()
        result = []
        
        # First traversing through K in the nums and only adding maximum value's index to the deque.
        # Note: We are olny storing the index and not the value.
        # Now, Comparing the new value in the nums with the last index value from deque,
        # and if new valus is less, we don't need it

        for windowEND in range(k):
            # HOLD THE INDEX OF THE LARGEST NUMBER IN THE QUEUE, SO IF THERE ARE SMALLER NUMBERS PRESENT, DELETE THEM
            while largestElements and nums[windowEND] > nums[largestElements[-1]]: largestElements.pop()
 
            largestElements.append(windowEND)
        
        # Here we will have deque with index of maximum element for the first subsequence of length k.

        # Now we will traverse from k to the end of array and do 4 things
        # 1. Appending left most indexed value to the result
        # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
        # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
        # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
 
        for windowEND in range(k, len(nums)):
            
            windowSTART = windowEND - k + 1
            
            # PROCESS THE PREVIOUS WINDOW FIRST
            result.append(nums[largestElements[0]])
            
            # NOW CHECK TO SEE IF THE MAX YOU HAVE STORED IS VALID TO USE FOR THIS CURRENT WINDOW
            if largestElements[0] < windowSTART: largestElements.popleft()
            
            # REMOVE ANY SMALLER ELEMENTS IF THERE ARE ANY
            while largestElements and nums[windowEND] > nums[largestElements[-1]]: largestElements.pop()
             
            # NOW THAT WE HAVE REMOVED ALL THE SMALLER ELEMENTS, WE CAN FINALLY ADD THE NEW ELEMENT
            largestElements.append(windowEND)
        
        # PROCESS THE LAST WINDOW
        result.append(nums[largestElements[0]])
        
        return result


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
 
        
        windowSTART = 0
        windowMaxes = []
        queue = collections.deque()
        
        for windowEND in range(len(nums)):
            
    
            windowSize = windowEND - windowSTART + 1 
            
            # Add current Element
            while queue and nums[queue[-1]] < nums[windowEND]:
                queue.pop()
                
            queue.append(windowEND)
            
            # remove last element if needed
            if queue and queue[0] <= windowEND - k:
                queue.popleft()
                
            # Add the max from the queue for this window
            if windowSize == k:
                windowMaxes.append(nums[queue[0]])
                windowSTART += 1
                
        return windowMaxes
            
            
            
                
            
            
a = Solution2().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
            