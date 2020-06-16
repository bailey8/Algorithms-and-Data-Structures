# So to find the combinations of 3 numbers, he is iterating through the list with the first pointer,
# and then trying to find two extra numbers to sum to 0. Since the list is ordered,
# the right pointer will always be higher than the middle pointer.
# So if the sum is too large, you can move the right pointer back one.
# On the other hand, if the sum is too small (below 0), then move the middle pointer up one.

# https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).


class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        # Need at least 3 numbers to contine
        for i in range(length-2):  # [8]
            # Since list is sorted, we know a positive element will never be 0.
            if nums[i] > 0:
                break
            # if number is same as previous number, then we will just get duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue  # [1]
            # Set up the 2 pointers, at the end and beginning
            l, r = i+1, length-1  # [2]
            while l < r:
                total = nums[i]+nums[l]+nums[r]

                if total < 0:  # [3]
                    l += 1
                elif total > 0:  # [4]
                    r -= 1
                else:  # [5]
                    res.append([nums[i], nums[l], nums[r]])
                    # Make sure you don't include duplicates
                    while l < r and nums[l] == nums[l+1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r-1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
            return res

            
class Solution(object):
    def threeSum(self, nums):

        nums.sort()
        output_array = []

        for i in range(0,len(nums) -2):
            
            # IF WE FOUND A DUPLICATE THEN WE ARE JUST GOING TO SKIP 
            if i > 0 and nums[i] == nums[i-1]: continue

            lower_boundary = i+1
            higher_boundary = len(nums)-1

            # THIS IS THE TARGET NUMBER WE WANT THE 2SUM TO ADD UP TO
            # THIS IS BC THAT WILL MAKE TOTAL SUM EQUAL 0 ADDING IN NUMS[I]
            targetSum = 0 - nums[i]

            while lower_boundary < higher_boundary:

                if nums[lower_boundary] + nums[higher_boundary] == targetSum:
                    
                    # APPEND ANSWER
                    output_array.append([nums[i],nums[lower_boundary],nums[higher_boundary]])
                    
                    # SKIP PAST DUPLICATES
                    while lower_boundary < higher_boundary and nums[lower_boundary] == nums[lower_boundary+1]: lower_boundary += 1
                    while lower_boundary < higher_boundary and nums[higher_boundary] == nums[higher_boundary-1]: higher_boundary -= 1
                        
                    # UPDATE WINDOW
                    lower_boundary += 1
                    higher_boundary -= 1
                    
                    

                # IF THE SUM IS TOO BIG, THEN SHRINK IT. SINCE ARRAY IS IN SORTED ORDER WE JUST DECREMENT THE LEFT POINTER
                elif nums[lower_boundary] + nums[higher_boundary] > targetSum:
                    higher_boundary -= 1

                # IF THE SUM IS TOO SMALL, THEN EXPAND IT. SINCE ARRAY IS IN SORTED ORDER WE JUST INCCREMENT THE RIGHT POINTER
                else:
                    lower_boundary += 1

        return output_array



a = Solution2()
b = [2,-1,-1]
print(a.threeSum(b))
 

    
                
                
