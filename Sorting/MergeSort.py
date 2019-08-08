# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)/2 # Finding the mid of the array
#         l = arr[:mid]  # Dividing the array elements
#         r = arr[mid:]  # into 2 halves
#
#         mergeSort(l)  # Sorting the first half
#         mergeSort(r)  # Sorting the second half
#
#         i = j = k = 0
#
#         while i < len(l) and j < len(r):
#             if l[i] < r[j]:
#                 arr[k] = l[i]
#                 i += 1
#             else:
#                 arr[k] = r[j]
#                 j += 1
#             k += 1
#
#             # Checking if any element was left
#         while i < len(l):
#             arr[k] = l[i]
#             i += 1
#             k += 1
#
#         while j < len(r):
#             arr[k] = r[j]
#             j += 1
#             k += 1

# Keep splitting the array until there are just 1 element pieces, and then pieces together
# def mergeSort(arr):
#     if len(arr)>1:
#         mid = len(arr)//2
#         l = arr[:mid]
#         r = arr[mid:]
#         mergeSort(l)
#         mergeSort(r)
#         i = j = k = 0
#         while i < len(l) and j < len(r):
#             if l[i] < r[j]:
#                 arr[k] = l[i]
#                 i +=1
#             else:
#                 arr[k] = r[j]
#                 j+=1
#             k +=1
#         while i < len(l):
#             arr[k] = l[i]
#             i +=1
#             k +=1
#         while j < len(r):
#             arr[k] = r[j]
#             j +=1
#             k +=1

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        r = arr[mid:]
        l = arr[:mid]
        mergeSort(r)
        mergeSort(l)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i +=1
            else:
                arr[k] = r[j]
                j +=1
            k +=1
        while i < len(l):
            arr[k] = l[i]
            i +=1
            k +=1
        while j < len(r):
            arr[k] = r[j]
            j +=1
            k +=1
    
a = [9, 8, 7, 6]
mergeSort(a)
print(a)
