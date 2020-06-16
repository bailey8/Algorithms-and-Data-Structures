class Solution:
    def search(self, nums,target):
    
        def find_Pivot(nums):
       
            left,right = 0, len(nums)-1
        
            # THE FIRST ELEMENT IS THE PIVOT [1(PIVOT),2,3,4] (<= CATCHES THE SINGLE ARRAY EDGE CASE EX) [1] - DRAW IT OUT!!!)
            if nums[left] <= nums[right]: return 0
            
            while left <= right:
                
                mid = (left+right)//2
                
                # [3,4,5(PIVOT),1,2]
                if nums[mid] > nums[mid+1]: return mid+1
                # If we don't encompass the pivot -> encompass the pivot
                # [5,6,7,8,9,10 (pivot),13,1,2,3,4] -> [13,1,2 (pivot),3,4] -> [13,1] -> base case hit
                elif nums[left] <= nums[mid]: left = mid+1
                #If we do encompass the pivot, then stay in pivot window
                else: right = mid-1
            
            return -1
        
        def bst(nums,target,l,r):
            while l<= r:
                mid = (l+r)//2
                if target == nums[mid]: return mid
                elif target < nums[mid]: r = mid-1
                else: l = mid+1
            return -1
                    
        # IF THERE IS NO ARRAY PASSED IN
        if not nums: return -1
         
        # FIND THE INDEX OF THE PIVOT
        pivot = find_Pivot(nums)
       
        # if array is not rotated, search in the entire array LIKE NORMAL
        if pivot == 0: return bst(nums,target, 0, len(nums)-1)
        
        # If the element is to the right of the pivot [10,11,12,1,2,3,4] then search that zone
        #If not, search the zone to the left, up to and including the pivot
        return bst(nums,target, pivot, len(nums)-1) if target < nums[0] else bst(nums,target, 0, pivot)


 
class Solution:
    def search(self, nums,target):
        start, end = 0, len(nums) - 1
        while start <= end:
            
            # STANDARD BINARY SEARCH PROCEDURE
            mid = (start+end) // 2
            
            # return mid if match
            if nums[mid] == target:
                return mid
            
            # OUR WINDOW EITHER ENCOMPASSES OR DOES NOT ENCOMPASS THE PIVOT
            # This means we are not encompassing the pivot in current window 
            # [1,2,3,4,5,-1] would trigger this case
            elif nums[start] <= nums[mid]:
                
                
                # ----- IF THE ELEMENT IS IN OUR CURRENT ZONE, THEN LETS STAY IN THE ZONE ---------- #
                # NORMAL BINARY SEARCH HERE
                #If the target is greater than the beginning of window but less than 
                # end of window then we know its between the window
                #[1,2,3,4,-1] searching for 2 would trigger this
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1

                # ----- IF THE ELEMENT IS NOT IN OUR CURRENT ZONE, THEN LETS TRY THE OTHER ZONE ------#
                #If that isn't the case then that means jump ahead to new window
                # [1,2,3,4,-1] searching for -1 wold trigger this
                else:
                    start = mid + 1
                    
             
            else:
                
                # ----- PROCEED TO SEARCH THE WINDOWS AS NORMAL, EXCEPT NOW WE SPECIFY WITH START AND END BC PIVOT MESSES WITH STUFF ------#
                # IF THE ELEMENT IS IN THE LEFT HALF THEN PROCEED AS NORMAL
                # [10,1,2,3,4,5,6,7,8,9] searching for 9 would trigger this # ------- we KNOW (KNOW) KNOW that the right side of the array contains the pivot ------#
                if target >= nums[mid] and target <= nums[end]: #[4, 5(mid), 6,7 (target),8(end)] we want to stay in the window if searching for 7
                    start = mid + 1
                # [10,1,2,3,4,5,6,7,8,9] searching for 10 would trigger this
                else:
                    end = mid - 1
        return -1


class Solution:
    def search(self, nums,target):

        left, right  = 0, len(nums) - 1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target: return mid
            
            
            # IF THE PIVOT IS THE FIRST HALF, CHECK AGAINST THE SECOND HALF
            if nums[left] > nums[mid]:
                # CHECK AGAINST THE SECOND HALF
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            
            # IF THE PIVOT IS THE SECOND HALF, CHECK AGAINST THE FIRST HALF
            else:
                # CHECK AGAINST THE FIRST HALF
                if nums[left] <= target < nums[mid]: right = mid-1
                else: left = mid + 1
            
        return -1
        
class Solution:
    def search(self, nums,target):
        start, end = 0, len(nums) - 1
        while start <= end:
            
            # STANDARD BINARY SEARCH PROCEDURE
            mid = (start+end) // 2
            
            # return mid if match
            if nums[mid] == target:
                return mid
            
            # OUR WINDOW EITHER ENCOMPASSES OR DOES NOT ENCOMPASS THE PIVOT
            # This means we are not encompassing the pivot in current window 
            # [1,2,3,4,5,-1] would trigger this case
            elif nums[start] <= nums[mid]:
                
                
                # ----- IF THE ELEMENT IS IN OUR CURRENT ZONE, THEN LETS STAY IN THE ZONE ---------- #
                # NORMAL BINARY SEARCH HERE
                #If the target is greater than the beginning of window but less than 
                # end of window then we know its between the window
                #[1,2,3,4,-1] searching for 2 would trigger this
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1

                # ----- IF THE ELEMENT IS NOT IN OUR CURRENT ZONE, THEN LETS TRY THE OTHER ZONE ------#
                #If that isn't the case then that means jump ahead to new window
                # [1,2,3,4,-1] searching for -1 wold trigger this
                else:
                    start = mid + 1
                    
             
            else:
                
                # ----- PROCEED TO SEARCH THE WINDOWS AS NORMAL, EXCEPT NOW WE SPECIFY WITH START AND END BC PIVOT MESSES WITH STUFF ------#
                # IF THE ELEMENT IS IN THE LEFT HALF THEN PROCEED AS NORMAL
                # [10,1,2,3,4,5,6,7,8,9] searching for 9 would trigger this
                if nums[mid] <= target <= nums[end]: 
                    start = mid + 1
                # [10,1,2,3,4,5,6,7,8,9] searching for 10 would trigger this
                else:
                    end = mid - 1
        return -1



class Solution69:
    def search(self, nums,target):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            
            # STANDARD BINARY SEARCH PROCEDURE
            mid = (start+end) // 2
            
            # return mid if match
            if nums[mid] == target: return mid
            
            #pivot is on the right side
            if nums[start] > nums[mid]:
                if nums[mid] < target <= nums[end]: 
                    start = mid+1
                else: 
                    right = mid-1
            else:
                if nums[start] <= target < nums[mid]:
                    right = mid-1
                else:
                    start = mid+1
              
            
        return -1

print(Solution69().search([4,5,6,7,0,1,2],0))