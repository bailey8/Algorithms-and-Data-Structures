# Option 1 is to store all the numbers in resizable array, and every time 
# the median is requested, sort container and output median

# Time complexity: O(nlogn)+O(1)≃O(nlogn).

# Adding a number takes amortized O(1) time for a container with an efficient resizing scheme.
# Finding the median is primarily dependent on the sorting that takes place. This takes O(nlogn) time for a standard comparative sort.

class MedianFinder():
    nums = []
    def __init__(self,arr):
        self.nums = arr
    def addNum(self,num):
        self.nums.append(num)
    
    def findMedian(self):
        self.nums.sort()
        if len(self.nums)%2 == 0:
            return (self.nums[len(self.nums)//2] + self.nums[(len(self.nums)//2)-1]) * .5
        return self.nums[len(self.nums)//2]


median = MedianFinder([])
print(median.findMedian())

# ---------------------------------------------------------------------------------------
# Option 2 is to use insertion sort after every insertion
# Complexity Analysis

# Time complexity:O(n)+O(logn)≈O(n).

# Binary Search takes O(logn) time to find correct insertion position.
# Insertion can take up to O(n) time since elements have to be shifted inside the container to make room for the new element.

# Use BS to find insertion point
# Shift all higher elements up by one space after insertion
# Effective when amount of insertion queries is less than amount of median queries

# --------------------------------------------------------------------------------
#Option 3, maintain direct access to median elements at all times. Allows finding median to take
# constant time. WE ONLY need a consistant way to access the median elements
# Keeping input array sorted is not a requirement.

# Max heap lo to store smaller half of elements.
# Min heap hiigh to store larger half
# max-heap can store at worst, one more element than min heap

# This gives us the nice property that when the heaps are perfectly balanced, 
# the median can be derived from the tops of both heaps. Otherwise, 
# the top of the max-heap lo holds the legitimate median.
import heapq
 
 