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
            #Since list is sorted, we know a positive element will never be 0.
            if nums[i] > 0:
                break
            #if number is same as previous number, then we will just get duplicates
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
                    #Make sure you don't include duplicates
                    while l < r and nums[l] == nums[l+1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r-1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
            return res


 
            
            