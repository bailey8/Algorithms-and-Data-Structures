
def quickSort(list):
    quickSortHelper(list,0,len(list)-1)

def quickSortHelper(list,start,end):
    if(start < end):
        split= partition(list,start,end)
        quickSortHelper(list,start,split-1)
        quickSortHelper(list,split+1,end)

def partition(list,start,end):
    pivot = list[start]
    i = start+1
    j = end
    while(i<=j):
        while(i<=j and list[i] <= pivot):
            i +=1
        while(j>=i and list[j] >= pivot):
            j -= 1
        if(i<=j):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    list[start] = list[j]
    list[j] = pivot
    return j



list  = [5,1,2,3,4]
quickSort(list)
print(list)
#
#
#
#
