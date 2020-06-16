class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        windowSTART = 0
        windowTotal = 0
        smallestWindow = float('inf')
        
        for windowEND in range(len(nums)):
            
            windowTotal += nums[windowEND]
            
            # IF WE HAVE HIT OUR TARGET, THEN SHRINK THE WINDOW AND SEE IF WE STILL HIT IT!
            while windowTotal >= s:
                smallestWindow = min(smallestWindow, windowEND-windowSTART+1)
                windowTotal -= nums[windowSTART]
                windowSTART += 1
            
        return 0 if smallestWindow == float('inf') else smallestWindow
            
            
        