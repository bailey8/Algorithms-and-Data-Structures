class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        leftPtr, rightPtr = 0, len(height)-1
        
        # WHILE OUR POINTERS HAVE NOT INTERSECTED
        while leftPtr < rightPtr:
            
            # MAXAREA IS THE THE NEW WINDOW WE HAVE OR THE OLD MAX WE HAD
            maxArea = max(min(height[rightPtr],height[leftPtr]) * (rightPtr- leftPtr) , maxArea)
            
            # WE ONLY WANT TO INCREMENT/DECREMENT THE PTR THAT HAS THE LOWEST HEIGHT, BC THAT IS OUR LIMITING FACTOR
            if height[rightPtr] <= height[leftPtr]: rightPtr -=1
            else: leftPtr += 1
        
        #RETURN THE LARGEST AREA WE FOUND SO FAR
        return maxArea

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxarea = 0
        
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                maxarea = max(maxarea, min(height[i], height[j]) * (j - i))
                
        return maxarea;