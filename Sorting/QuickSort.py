
# def quickSort(list):
#     quickSortHelper(list,0,len(list)-1)

# def quickSortHelper(list,start,end):
#     if(start < end):
#         split= partition(list,start,end)
#         quickSortHelper(list,start,split-1)
#         quickSortHelper(list,split+1,end)

# def partition(list,start,end):
#     pivot = list[start]
#     i = start+1
#     j = end
#     while(i<=j):
#         while(i<=j and list[i] <= pivot):
#             i +=1
#         while(j>=i and list[j] >= pivot):
#             j -= 1
#         if(i<=j):
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
#     list[start] = list[j]
#     list[j] = pivot
#     return j

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

# def quicksort(list):
#     quickSortHelper(list,0,len(list)-1)
# def quickSortHelper(list,start,end):
#     if start < end:
#         split = partition(list,start,end)
#         quickSortHelper(list,start, split-1)
#         quickSortHelper(list,split+1, end)
# def partition(list,start,end):
#     l= f =  start
#     while l< end:
#         if list[l] < list[end]:
#             list[l],list[f] =list[f], list[l]
#             f +=1
#         l+=1
#     list[f], list[end] = list[end],list[f]
#     return f

def quicksort(list):
    quicksorthelper(list,0,len(list)-1)
def quicksorthelper(list,start,end):
    if start < end:
        






list  = [5,1,2,3,4,99,-3,0,0,0]
quicksort(list)
print(list)
#
#
#
#
