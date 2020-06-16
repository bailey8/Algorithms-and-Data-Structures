class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # THE MAX SUM WE HAVE SO FAR
        maximum = float('-inf')
        # THE SUM OF OUR CURRENT TRACKING WINDOW
        currSum = 0
        
        # FOR EVERY NUMBER
        for i in range(len(nums)):
            
            # ADD THIS NUMBER TO OUR CURRENT WINDOW SUM
            currSum += nums[i]
            # IF THIS SUM IS BETTER THAN OUR PREVIOUS BEST, THEN UPDATE OUR GLOBAL BEST
            maximum = max(currSum,maximum)

            # IF THE ARRAY 
            if currSum < 0: currSum = 0
            
        return maximum



class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        
        # THE BIGGEST SUM SO FAR IS THE FIRST ELEMENT
        max_sum = nums[0]
        for i in range(1, len(nums)):
            # IF IT IS POSITIVE THEN IT WILL ADD TO THE CURRENT SUM NO MATTER WHAT
            # IF IT IS NEGATIVE, THEN WHY TF WOULD WE KEEP IT???? WE WOULDNT. WE START FRESH
            # BY NOT CHANGING NUMS[i] IF THE PREV SUM IS NEGATIVE, WE EFFECTIVLEY RESTART THE SUM AS THE CURRENT ELEMENT WE ARE ON
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            
            # SEE IF OUR CURRENT SUM IS BIGGER OR SMALLER THAN THE PREV BEST
            max_sum = max(nums[i], max_sum)
        
        return max_sum

#DP SOLUTION
class Solution3:
    def maxSubArray(self, nums):
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] +nums[i],nums[i])
        return max(dp)

 # GREEDY SOLUTION
class Solution2:

    def maxSubArray(self, nums):
        
        curr_sum = max_sum = float('-inf')

        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
            
        for i in range(1, len(nums)):
           
            # KEEP A RUNNING TOTAL OF THE MAX SUM AT EACH INDEX
            nums[i] = max(nums[i] + nums[i-1], nums[i])
        
        # DO ANOTHER PASS THROUGH TO EXTRACT THE MAX IN THE CACHE
        return max(nums)



