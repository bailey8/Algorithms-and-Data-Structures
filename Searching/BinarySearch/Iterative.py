def binarySearch(arr, left, right, x): 
  
    while left <= right: 
  
        mid = left + (right - left)/2
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            left = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            right = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1
  
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 