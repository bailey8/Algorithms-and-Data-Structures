
 

# def quicksort(arr):
#     quicksortHelper(arr,0,len(arr)-1)
# def quicksortHelper(arr,start,end):
#     if start < end:
#         split = partition(arr,start,end)
#         quicksortHelper(arr, start,split-1)
#         quicksortHelper(arr,split+1,end)
# def partition(arr,start,end):
#     f = l = start
#     while l < end:
#         if arr[l] < arr[end]:
#             arr[f],arr[l] = arr[l], arr[f]
#             f +=1
#         l +=1
#     arr[end],arr[f] = arr[f],arr[end]
#     return f

# def quicksort(arr):
#     quickSortHelper(arr,0,len(arr)-1)
# def quickSortHelper(arr,start,end):
#     if start < end:
#         split = partition(arr,start,end)
#         quickSortHelper(arr,start, split-1)
#         quickSortHelper(arr,split+1, end)
# def partition(arr,start,end):
#     l= f =  start
#     while l< end:
#         if arr[l] < arr[end]:
#             arr[l],arr[f] =arr[f], arr[l]
#             f +=1
#         l+=1
#     arr[f], arr[end] = arr[end],arr[f]
#     return f

def quicksort(arr):
    quicksortHelper(arr,0,len(arr)-1)
def quicksortHelper(arr,start,end):
    if start < end:
        split = partition(arr,start,end)
        quicksortHelper(arr,start,split-1)
        quicksortHelper(arr,split+1,end)
def partition(arr,start,end):
    f = l = start
    pivot = arr[end]
    while l < end:
        if arr[l] < pivot:
            arr[f],arr[l] = arr[l],arr[f]
            f +=1
        l+=1
    arr[end],arr[f] = arr[f],arr[end]
    return f

arr = [1,2,3,4,5,-99]
quicksort(arr)
print(arr)

print(3//2)