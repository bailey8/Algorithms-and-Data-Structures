class Solution:
    def search_quadruplets(self, arr, target):
        arr.sort()
        quadruplets = []
        for indexFIRST in range(0, len(arr)-3):

            if indexFIRST > 0 and arr[indexFIRST] == arr[indexFIRST - 1]: continue

            for indexSECOND in range(indexFIRST + 1, len(arr)-2):
                
                if indexSECOND > indexFIRST + 1 and arr[indexSECOND] == arr[indexSECOND - 1]: continue

                search_pairs(arr, target, indexFIRST, indexSECOND, quadruplets)

        return quadruplets


def search_pairs(arr, target_sum, first, second, quadruplets):
    
    left, right = second + 1, len(arr) - 1

    while (left < right):

        totalSum = arr[first] + arr[second] + arr[left] + arr[right]

        if totalSum == target_sum:  # found the quadruplet
            quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while (left < right and arr[left] == arr[left - 1]): left += 1
            while (left < right and arr[right] == arr[right + 1]): right -= 1

        elif totalSum < target_sum: left += 1   
        else: right -= 1


def main():
  print(Solution().search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(Solution().search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
