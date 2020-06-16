
class Solution:
    def nextPermutation(self,nums):

        # Grab the index of the 2nd to last element in the array
        smallIndexBeforeDecrease = len(nums) - 2

        """
        Walk backwards. Keep walking until we reach the point right
        before the decreasing sequence begins. When this while loop
        ends that is where i will stand
        """
        # FIND THE FIRST INDEX WHERE THE ELEMENT AHEAD IS BIGGER, WHICH MEANS THE SEQUENE IS DECREASING
        # 1 2 3 4 10 9 6
        while smallIndexBeforeDecrease >= 0 and nums[smallIndexBeforeDecrease] >= nums[smallIndexBeforeDecrease + 1]:
            smallIndexBeforeDecrease -= 1


        """
        If i is not the first element we have more work to do

        If i IS the first element we just skip down to reverse
        the whole array since the WHOLE array would be decreasing
        meaning we are on our last permutation
        """
        if smallIndexBeforeDecrease >= 0:

            """
                Start a pointer at the end of the array, we want to search for
                the smallest item THAT IS GREATER THAN THE ELEMENT AT i
                Why? Why Why Why. The reason why is that we want to know the
                NEXT element that is to be planted where i is sitting. THIS
                WILL ROOT THE NEXT PERMUTATION and represents the smallest change
                we can make thus ensuring we have exactly the next permutation
            """
            smallestPossibleChange = len(nums) - 1

            # THE FIRST ELEMENT THAT IS GREATER THAN THE SWAP POINT WILL BE USED.
            while smallestPossibleChange >= 0 and nums[smallestPossibleChange] <= nums[smallIndexBeforeDecrease]:
                smallestPossibleChange -= 1

            """
                We swap those elements.

                Now all that is left is to reverse the decreasing section (it
                is already sorted in reverse order) to restore it to the first
                positionality it would be with the new value rooted at i
            """
            self.swap(nums, smallIndexBeforeDecrease, smallestPossibleChange)

        """
        Perform the reversal on the decreasing section now. We pass in i + 1
        since i sits RIGHT BEFORE the decreasing section that is on its final
        permutation
        """
        self.reverse(nums, smallIndexBeforeDecrease + 1)

    def reverse(self, nums, start):
        left = start
        right = len(nums) - 1

        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


a = [None]

if not a[0]: print(a[0])