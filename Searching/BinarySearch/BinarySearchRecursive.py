def binarySearch (arr, left, right, x): 
  
    # Check base case 
    if right >= left: 
  
        mid = left + (right - left)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, left, mid-1, x) 
  
        # Eleftse the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, right, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
result = binarySearch(arr, 0, len(arr)-1, x) 