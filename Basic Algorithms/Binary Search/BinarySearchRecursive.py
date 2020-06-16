# Iterative Binary search only has O(1) space complexity, where recursive has O(logn)
# def binary_search(list, num):
#     l = 0
#     r = len(list)-1
#     while l <= r:
#         current = (l+r)//2
#         if list[current] < num:
#             l = current+1
#         elif list[current] > num:
#             r = current-1
#         else:
#             return current
#     return None


# def bSearch(arr,target,l,r):
#     if l <= r:
#         mid = (l+r)//2
#         if arr[mid] > target: return bSearch(arr,target,l,mid-1)
#         elif arr[mid] < target: return bSearch(arr,target,mid+1,r)
#         else: return mid
    
#     return -1

# print(bSearch([1, 2, 3, 4, 5], 1,0,4))




# def recursiveBS(list, l, r, x):
#     if(l > r):
#         return -1
#     else:
#         mid = (l+r)//2
#         if list[mid] > x:
#             r = mid-1
#         elif list[mid] < x:
#             l = mid+1
#         else:
#             return mid
#         return recursiveBS(list, l, r, x)

# def recursiveBS(arr,l,r,x):
#     if l > r:
#         return None
#     mid = (l+r)//2
#     if arr[mid] < x:
#         l = mid+1
#     elif arr[mid] > x:
#         r = mid-1
#     else:
#         return mid
#     return recursiveBS(arr,l,r,x)

 




# def recursiveBS(arr,l,r,target):
    
#     #BASE CASE
#     if r < l: return False

#     middle = (l+r)//2
#     if target < arr[middle]:
#         return recursiveBS(arr,l,middle-1,target)
#     elif target > arr[middle]:
#         return recursiveBS(arr,middle+1,r,target)
#     else:
#         return True

# def recursiveBS2(arr,l,r,target):

#     # BASE CASE
#     if r < l: return None

#     middle = (l+r)//2
#     if target < arr[middle]:
#         r = middle -1
#     elif target > arr[middle]:
#         l = middle+1
#     else:
#         return middle
    
#     return recursiveBS2(arr,l,r,target)

# def iterative(arr,num):
#     l,r = 0,len(arr)-1
#     while r >=l:
#         mid = (r+l)//2
#         if num < arr[mid]:
#             r = mid-1
#         elif num > arr[mid]:
#             l = mid+1
#         else:
#             return mid
#     return None

def binary_search(arr,num):
    l,r = 0, len(arr)-1

    # IT IS OKAY FOR THESE TO BE EQUAL
    while l <=r:
        mid = (l+r)//2
        print(f'left:{l} mid:{mid} right:{r}')
        if arr[mid] < num:
            l = mid+1
        elif arr[mid] > num:
            r = mid-1
        else:
            return mid
    return None

binary_search([1,2,3,4,5],2)


# print(recursiveBS2([1, 2, 3, 4, 6], 0, 4, 5))
# print(iterative([1, 2, 3, 4, 9], 3))




