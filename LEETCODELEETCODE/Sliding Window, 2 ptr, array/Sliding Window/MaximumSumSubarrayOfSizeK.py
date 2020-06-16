def max_sub_array_of_size_k(k, arr):
  
    largest = float('-inf')
    windowTotal = windowSTART = 0

    for windowEND in range(len(arr)):

        windowTotal += arr[windowEND]

        # IF THIS IS A VALID WINDOW, THEN UPDATE MAX SUM
        if windowEND - windowSTART + 1 == k:
            largest = max(largest, windowTotal)
            windowTotal -= arr[windowSTART]
            windowSTART += 1
    
    return largest


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))) # 9
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))) # 7

main()


# BRUTE FORCE
def max_sub_array_of_size_k(k, arr):
    
    largestWindow = 0
    currentWindowSum = 0

    for windowSTART in range(len(arr) - k + 1):
        currentWindowSum = 0
        for windowEND in range(windowSTART, windowSTART+k):
            currentWindowSum += arr[windowEND]
            largestWindow = max(largestWindow, currentWindowSum)
    return largestWindow

