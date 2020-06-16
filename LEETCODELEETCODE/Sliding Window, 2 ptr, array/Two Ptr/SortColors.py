def dutch_flag_sort(arr):
    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low < i are 1
    leftPTR, rightPTR = 0, len(arr) - 1
    centerIndex = 0


    while(centerIndex <= rightPTR):
        if arr[centerIndex] == 0:
            arr[centerIndex], arr[leftPTR] = arr[leftPTR], arr[centerIndex]
            # increment 'i' and 'low'
            centerIndex += 1
            leftPTR += 1
        elif arr[centerIndex] == 1:
            centerIndex += 1
        else:  # the case for arr[i] == 2
            arr[centerIndex], arr[rightPTR] = arr[rightPTR], arr[centerIndex]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            rightPTR -= 1


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
