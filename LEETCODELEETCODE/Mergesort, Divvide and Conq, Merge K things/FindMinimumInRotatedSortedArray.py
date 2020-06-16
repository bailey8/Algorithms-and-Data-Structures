
class Solution:
    def findMin(self, nums: List[int]) -> int:
                
        l,r = 0, len(nums)-1
        
        if nums[l] <= nums[r]: return nums[l]
        
        while l <= r:
            
            mid = (l+r)//2
            
            # this means the pivot is the element ahead
            if nums[mid] > nums[mid+1]: return nums[mid+1]
            
            #  we are in the window, so escape the window
            if nums[l] <= nums[mid]: l = mid+1 #[2,3,4(mid),1] -> we can do mid+1 bc it would've been caught in first condition
            else: r = mid-1
            
class Solution:
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set left and right bounds
        left, right = 0, len(arr)-1
        
        # if arr[left] <= arr[right]: return arr[left] - NO NEED
        
        while left < right:
            
            mid = (left+right)//2
    
            # IF THE RIGHT BOUNDRY CONTAINS PIVOT THEN MOVE TO ENCOMPASS PIVOT
            if arr[mid] > arr[right]: left = mid + 1 #would fail on [0,1 (mid),2] or [5,1,2] or [5,6,1], [0,1], [1,0] <- CHECK THESE CASES
            # IF NOT MOVE TO ENCOMPASS PIVOT
            else: right = mid
            
        return arr[left]
        
        
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set left and right bounds
        left, right = 0, len(nums)-1
                
        # left and right both converge to the minimum index; 
        # DO NOT use left <= right because that would loop forever
        while left < right: # [10,11,12,1(converge),2,3,4]

            # find the middle value between the left and right bounds (their average)
            mid = (left + right) // 2
                        
            # the main idea for our checks is to converge the left and right bounds on the start
            # of the pivot, and never disqualify the index for a possible minimum value.

            # in normal binary search, we have a target to match exactly,
            # and would have a specific branch for if nums[mid] == target.
            # WE DO NOT HAVE A SPECIFIC TARGET HERE, WE JUST HAVE A SIMPLE IF/ELSE
                         
            if nums[mid] > nums[right]:
                # we KNOW the pivot must be to the right of the middle:
                # if nums[mid] > nums[right], we KNOW that the
                # pivot/minimum value must have occurred somewhere to the right
                # of mid, which is why the values wrapped around and became smaller.

                # example:  [3,4,5,6,7 (MID),8,9,1 (pivot),2] 
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] > nums[right], we know that at some point to the right of mid,
                # the pivot must have occurred, which is why the values wrapped around
                # so that nums[right] is less then nums[mid]

                # we know that the number at mid is greater than at least
                # one number to the right, SO WE CAN USE mid + 1 and
                # never consider mid again; we know there is at least
                # one value smaller than it on the right
                left = mid + 1

            else:
                # here, nums[mid] <= nums[right]:
                # we KNOW the pivot must be the middle or to the left of the middle:
                # if nums[mid] <= nums[right], we KNOW that the pivot was not encountered
                # to the right of middle, because that means the values would wrap around
                # and become smaller (which is caught in the above if statement).
                # this leaves the possible pivot point to be at index <= mid.
                            
                # example: [8,9,1(pivot),2,3(MID),4,5,6,7]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] <= nums[right], we know the numbers continued increasing to
                # the right of mid, so they never reached the pivot and wrapped around.
                # therefore, we know the pivot must at index <= mid.

                # we know that nums[mid] <= nums[right].
                # therefore, we know it is possible for the mid index to store a smaller
                # value than at least one other index in the list (at right), so we do
                # not discard it by doing right = mid - 1. it still might have the minimum value.
                right = mid # [3(left),1(mid),2(right)] <- would trigger this case!!!
                            # [3(left)(mid),1(right)] <- would trigger this case!!
                            # [3(left)]
                
        # at this point, left and right converge to a single index (for minimum value)
        # our if/else block forces the bounds of left/right to shrink each iteration:

        # when left bound increases, it does not disqualify a value
        # that could be smaller than something else (we know nums[mid] > nums[right],
        # so nums[right] wins and we ignore mid).

        # when right bound decreases, it also does not disqualify a
        # value that could be smaller than something else (we know nums[mid] <= nums[right],
        # so nums[mid] wins and we keep it for now).

        # so we shrink the left/right bounds to one value,
        # without ever disqualifying a possible minimum
        return nums[left]