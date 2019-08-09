# If nums[0] <= nums[i], then nums[0..i] is sorted (in case of "==" it's just one element, and in case of "<" there must be a drop elsewhere).
#  So we should keep searching in nums[0..i] if the target lies in this sorted range, i.e., if nums[0] <= target <= nums[i].

# If nums[i] < nums[0], then nums[0..i] contains a drop, and thus nums[i+1..end] is sorted and lies strictly between nums[i] and nums[0].
#  So we should keep searching in nums[0..i] i

#  THE PROBLEM IN NOT BEING ABLE TO DO REGULAR BINARY SEARCH IS: 
#  WHEN YOUR MID POINT AND TARGET END UP BEING IN DIFFERENT HALVES 

# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/154836/The-INF-and-INF-method-but-with-a-better-explanation-for-dummies-like-me
import math

class Solution(object):
    def search(self, nums, target):
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            comparator = nums[mid]
            if((target < nums[0]) and (nums[mid] < nums[0]) or (target >= nums[0]) and (nums[mid] >= nums[0])):
                comparator = nums[mid]
            else:
                if target < nums[0]:
                    comparator = -(math.inf)
                else:
                    comparator = math.inf
            if target == comparator: return mid
            if target > comparator:
                l = mid+1
            else
                r = mid-1
        return -1
       