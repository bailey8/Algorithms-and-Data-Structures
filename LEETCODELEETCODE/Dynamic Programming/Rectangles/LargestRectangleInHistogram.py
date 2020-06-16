class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
 
        maxarea = 0
    
        # FOR EACH BAR FROM LEFT TO RIGHT
        for i in range(len(heights)):
            #THIS IS THE MINIMUM HEIGHT OF A BAR
            minheight = float('inf')
            # NOW FIND THE RIGHT ENDPOINT (WE ARE CALCULATING ALL PAIRS REMEMBER)
            for j in range(i,len(heights)):
                
                # UPDATE THE MINIMUM IF NEEDED
                minheight = min(minheight, heights[j])
                
                #FOR EACH PAIR CALCULATE THE AREA AND UPDATE IF NEEDED
                maxarea = max(maxarea, minheight * (j - i + 1))
 
        return maxarea


# DIVIDE AND CONQUER
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def calculateArea(start, end):
            
            # BASE CASE
            if start > end: return 0
            
            #FIND THE INDEX THAT HAS A TOWER THAT IS THE SMALLEST HEIGHT
            minindex = start
            for i in range(start, end+1):
                if heights[minindex] > heights[i]:
                    minindex = i
            
            # DIVIDE INTO LEFT AND RIGHT SUBPROBLEMS
            currentWindowMaxSize = heights[minindex] * (end - start + 1)
            leftWindowMaxSize =  calculateArea(start, minindex - 1)
            rightWindowMaxSize = calculateArea(minindex + 1, end)
            
            return max(currentWindowMaxSize,leftWindowMaxSize,rightWindowMaxSize)
    
   
        return calculateArea(0, len(heights) - 1);