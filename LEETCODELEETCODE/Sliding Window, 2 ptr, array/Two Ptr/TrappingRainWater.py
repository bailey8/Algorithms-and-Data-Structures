class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        
        leftHighest = [i for i in height]
        rightHighest = [i for i in height]
        
        # POPULATE THE ARRAY FOR THE TALLEST TOWER TO THE LEFT AT EACH INDEX
        for index in range(1,len(height)):
            # the height is either previous max, or the height of the index itself
            # (the index height is taller than any tower we have previously seen)
            leftHighest[index] = max(leftHighest[index-1],height[index])
        
        
        # POPULATE THE ARRAY FOR THE TALLEST TOWER TO THE RIGHT AT EACH INDEX
        for index in reversed(range(len(height)-1)):
            # the height is either previous max, or the height of the index itself
            # (the index height is taller than any tower we have previously seen)
            rightHighest[index] = max(rightHighest[index+1],height[index])
            
        # THIS UNPACKS SHIT LIKE INDEX, (LEFTHIGHEST,RIGHTHIGHEST)
        for index,tup in enumerate(zip(leftHighest,rightHighest)):
            leftHighest, rightHighest = tup
            # for each tower, we have the tallest tower to the right and left.
            # Subtract the hight of the tower at the index itself to get units of water it can hold.
            #If tower is tallet than the tallest right/left towers, then we add 0 to total (not negative)
            total += max(0,min(leftHighest,rightHighest)- height[index])
        
        
        return total
            

class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        
        leftHighest = [i for i in height]
        rightHighest = [i for i in height]
        
        left,right = 1, len(height)-2
        # POPULATE THE ARRAY FOR THE TALLEST TOWER TO THE LEFT AT EACH INDEX
        for element in range(len(height)-1):
            # the height is either previous max, or the height of the index itself
            # (the index height is taller than any tower we have previously seen)
            leftHighest[left] = max(leftHighest[left-1],height[left])
            rightHighest[right] = max(rightHighest[right+1],height[right])
            left +=1
            right -=1

        
        # THIS UNPACKS SHIT LIKE INDEX, (LEFTHIGHEST,RIGHTHIGHEST)
        for index,tup in enumerate(zip(leftHighest,rightHighest)):
            leftHighest, rightHighest = tup
            # for each tower, we have the tallest tower to the right and left.
            # Subtract the hight of the tower at the index itself to get units of water it can hold.
            #If tower is tallet than the tallest right/left towers, then we add 0 to total (not negative)
            total += max(0,min(leftHighest,rightHighest)- height[index])
        
        
        return total

class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        leftHighest = [i for i in height]
         
        left = 1
        # POPULATE THE ARRAY FOR THE TALLEST TOWER TO THE LEFT AT EACH INDEX
        for leftPtr in range(1,len(height)):
            # the height is either previous max, or the height of the index itself
            # (the index height is taller than any tower we have previously seen)
            leftHighest[leftPtr] = max(leftHighest[leftPtr-1],height[leftPtr])
              
        # CALCULATE THE FINAL ANSWER IN ONE PASS
        rightHighest = 0
        for index in reversed(range(len(height))):
            # CALCULATE THE RIGHT HIGHEST ON THE FLY
            total += max(0,min(leftHighest[index],rightHighest)- height[index])
            rightHighest = max(height[index],rightHighest)
               
        return total
            
        
class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = rightMax = 0
        leftPtr, rightPtr = 0, len(height) -1
        
        total = 0
        
        while leftPtr < rightPtr:
            
            # THE LEFT TOWER IS SMALLER (WE ALREADY KNOW THE MAX HEIGHT TO THE LEFT OF THIS SIDE IS ALSO SMALLER THAN RIGHT TOWER)
            if height[leftPtr] < height[rightPtr]:
                # THIS TRACKS THE TALLEST TOWER ON THE LEFT SIDE
                if leftMax < height[leftPtr]: leftMax = height[leftPtr]
                total += leftMax - height[leftPtr]
                leftPtr += 1
            else:
                # THE RIGHT TOWER IS SMALLER (WE ALREADY KNOW THE MAX HEIGHT TO THE RIGHT OF THIS SIDE IS ALSO SMALLER THAN LEFT TOWER)
                # THIS TRACKS THE TALLEST TOWER ON THE RIGHT SIDE
                if rightMax < height[rightPtr]: rightMax = height[rightPtr]
                total += rightMax - height[rightPtr]
                rightPtr -= 1
        return total
                