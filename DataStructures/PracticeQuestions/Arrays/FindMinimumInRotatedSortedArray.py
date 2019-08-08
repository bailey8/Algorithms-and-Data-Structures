def findMin(arr):
    i = 0
    #keep iterating over until you find an element less than previous
    while i+1 < len(arr):
        if arr[i] > arr[i+1]:
            return arr[i+1]
        i += 1
    #if no element found, then the first element must be smallest
    return arr[0]



#looking for inflection point
#if first element is greater than last, then no pivot occured
def findMin2(nums):
    if nums[0] < nums[len(nums)-1]:
        return nums[0]
    i,j = 0,len(nums)-1
    while i<= j:
        mid = (i+j)//2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid] < nums[mid-1]:
            return nums[mid]
# the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
        if nums[mid] > nums[0]:
            i = mid+1
        else:
            j = mid-1

print(findMin2([1,2,3,4,5,6,0]))



