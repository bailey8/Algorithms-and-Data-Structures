def length_of_longest_substring(arr, k):
  

    numberOfZeros = windowSTART = 0

    longest = 0

    for windowEND, rightNumber in enumerate(arr):

        if rightNumber == 0: numberOfZeros += 1

        while numberOfZeros > k:

            leftNum = arr[windowSTART]
            if leftNum == 0: numberOfZeros -= 1
            windowSTART += 1

        longest = max(longest, windowEND-windowSTART+1)

    return longest

def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)) # 6
  print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)) # 9


main()
