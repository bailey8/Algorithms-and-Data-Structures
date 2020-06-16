class Solution:
    def shortest_window_sort(self,arr):
        low, high = 0, len(arr) - 1

        # find the first number out of sorting order from the beginning
        while low < len(arr) - 1 and arr[low] <= arr[low + 1]: low += 1

        if low == len(arr) - 1:  return 0 # If array is sorted

        # find the first number out of sorting order from the end
        while high > 0 and arr[high] >= arr[high - 1]: high -= 1

        # find the maximum and minimum of the subarray
        subarray_max = float('-inf')
        subarray_min = float('inf')

        for k in range(low, high+1):
            subarray_max = max(subarray_max, arr[k])
            subarray_min = min(subarray_min, arr[k])

        # LARGER ELEMENTS MUST GO TO THE RIGHT
        while (low > 0 and arr[low-1] > subarray_min): low -= 1

        # SMALLER ELEMENTS MUST GO TO THE LEFT
        while (high < len(arr)-1 and arr[high+1] < subarray_max):
            high += 1

        return high - low + 1
