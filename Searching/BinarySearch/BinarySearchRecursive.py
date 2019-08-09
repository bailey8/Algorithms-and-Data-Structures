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

# def binary_search(arr,num):
#     l,r = 0, len(arr)-1
#     while l <=r:
#         mid = (l+r)//2
#         if arr[mid] < num:
#             l = mid+1
#         elif arr[mid] > num:
#             r = mid-1
#         else:
#             return mid
#     return None

def binary_search(arr,num):
    l =0 
    r = len(arr) -1
    while l <=r:
        mid = (l+r)//2
        if arr[mid] < num:
            l = mid+1
        elif arr[mid] > num:
            r = mid-1
        else:
            return mid
    return None




print(binary_search([1, 2, 3, 4, 5], 1))


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

def recursiveBS(arr,l,r,x):
    if l > r:
        return None
    mid = (l+r)//2
    if arr[mid] < x:
        l = mid +1
    elif arr[mid] > x:
        r = mid-1
    else:
        return mid
    return recursiveBS(arr,l,r,x)

    

print(recursiveBS([1, 2, 3, 4, 5], 0, 4, 5))
