# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
        
#         return return [i for i in sorted(nums)[:-1] if i+1 in nums][0]

class Solution:
    def missingNumber(self, nums):
        a = set(nums)
        for i in range(0,len(nums)+1):
            if i not in a:
                return i
class Solution:
    def missingNumber(self, nums):
        
        # THIS CONVERTS AN ITERABLE TO A SET
        num_set = set(nums)
        
        # INPUT IS GIVEN AS O....N WHICH MEANS N+1 NUMBERS
        n = len(nums) + 1
        
        # IF THE NUMBER IS NOT IN THE SET THEN WE KNOW THATS THE MISSING NUMBER
        for number in range(n):
            if number not in num_set:
                return number