class Solution:
    def removeDuplicates(self, nums) -> int:
        
        if not nums: return 0
        
        ptrLEFT = 0
        
        for ptrRIGHT in range(1,len(nums)):
            
            # if the elements are not duplicates
            if key != nums[ptrRIGHT]:
                
                # increment the "leftMostNonDuplicate" pointer
                ptrLEFT += 1
            
            # make the "leftmostNonDuplicate" equal to the right pointer
            # remember, if the right pointer is the same as the left ptr, then this wont really do anything..
            # But if the pointers are different then this will update nums with the first different character
            nums[ptrLEFT] = nums[ptrRIGHT]
                
        return ptrLEFT + 1
            
            
    