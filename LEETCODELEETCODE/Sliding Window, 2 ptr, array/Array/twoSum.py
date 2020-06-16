class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # ONE PASS DICTIONARY SOLUTION
        dic = {}
        for index,number in enumerate(nums):
            
            # IF THE COMPLEMENT IS IN DICTIONARY THEN WE ARE GOOD TO GO
            if target-number in dic:
                return [dic[target-number], index]
            
            #IF COMPLEMENT IS NOT IN DICTIONARY THEN WE ADD IT AND KEEP CHUGGINF
            dic[number] = index
            