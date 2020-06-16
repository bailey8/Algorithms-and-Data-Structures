class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def lengthofLIS(prev, index):
            
            # BASE CASE, we reached the end of array, so no more numbers added to sequence
            if index == len(nums): return 0

            taken = nottaken = 0
            
            # ---------AT EVERY NUMBER, WE MAKE THE CHOICE TO INCLUDE IT OR NOT TO INCLUDE IT ----------#
            
            # TO BUILD OFF THE CURRENT SEQUENCE, THE NUMBER MUST BE GREATER THAN THE LAST NUMBER IN THE SEQUENCE
                                    # THE PREVIOUS NUMBER IN THE SEQUENCE FOR THE NEXT ITERATION IS THIS ITERATIONS CURRENT NUMBER
            if nums[index] > prev: taken = 1 + lengthofLIS(nums[index], index + 1)

            # DONT INCLUDE THE CURRENT NUMBER, SO KEEP THE PREVIOUS NUMBER
            nottaken = lengthofLIS(prev, index + 1)
            
            return max(taken, nottaken)
 
        return lengthofLIS(float('-inf'), 0)
 
 
class Solution:
    def lengthOfLIS(nums):

        if len(nums) == 0: return 0

        # Array to store our subproblems, default answer is 1.
        maxLength = [1]*len(nums)
        #By default the best answer is a length of 1
        maximumSoFar = 1
        #Test every possible end index of a longest increasing subsequence
        for i in range(1,len(nums)):
        
            """
            We aim to see if we can append the item at nums[i]
            to extend the Longest Increasing Subsequence achieved
            from index 0...j (which is what the cache records)
            We want to solve for maxLength[i] if the value at 'i'
            beats 'j'. If we can we see which is greater between
            these then we have our answer:
            1.) maxLength[i]: The best answer so far for the LIS from 0...i
            2.) maxLength[j] + 1: The value of maxLength[j] is the length
            of the LIS from 0...j, we conceptually "append" this item to
            that LIS by adding 1 to that subproblem answer, yielding a
            potentially new answer for LIS[0..i]
            """

            for j in range(i):
                if nums[i] > nums[j]:
                    maxLength[i] = max(maxLength[i], maxLength[j] + 1)
                
        #We now have an answer for LIS[0...i]. Compete it against the best LIS length found so far.
    
    return max(maxLength)


# ----------------------------------------recursion with memo
# class Solution:
#     def lengthOfLIS(self,nums):
    
#         def lengthofLIS(previndex, index):
            
#             if index == len(nums): return 0
#             if memo[previndex + 1][index] >= 0:
#                 return memo[previndex + 1][index]
#             taken = 0
#             if previndex < 0 or nums[index] > nums[previndex]:
#                 taken = 1 + lengthofLIS(index, index + 1)
            

#             nottaken = lengthofLIS(previndex, index + 1)
#             memo[previndex + 1][index] = max(taken, nottaken)
#             return memo[previndex + 1][index]
            
#         memo = [[-1 for _ in range(len(nums))] for _ in range(len(nums)+1)]
#         return lengthofLIS(-1, 0)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = [1] * len(nums)
        
        # THIS IS WHERE WE PLANT
        for PLANT in range(len(nums)):
            
            # CHECK ALL NUMBERS TO THE LEFT
            for leftIndex in range(PLANT):
                
                #IF THE NUMBER IS SMALLER, THEN ADD ITS SUBSEQUENCE LENGTH TO OURS!!!
                if nums[PLANT] > nums[leftIndex]:
                    
                    # ONLY KEEP THE LARGEST SUBSEQUENCE
                    cache[PLANT] = max(cache[PLANT], 1 + cache[leftIndex])
                    
        return max(cache) if nums else 0