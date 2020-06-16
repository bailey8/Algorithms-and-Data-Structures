def insertionSort(arr):
    for i in range(1,len(arr)):
        #This is why its good on sorted data, if data is sorted then it
        #will ignore this inner while loop and outer while loop runs O(n)
        #times so the algo is best case O(n)
        while i > 0 and arr[i-1] > arr[i]:
            arr[i],arr[i-1] = arr[i-1], arr[i]
            i -=1
    print(arr)

 

arr = [10,9,8,0,7]
insertionSort(arr)
