class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0: return 0
        if n < 4: return max(nums)

        twoHousesBack, oneHouseBack = 0, 0
        for i in nums[:-1]: 
            twoHousesBack, oneHouseBack = oneHouseBack, max(twoHousesBack + i, oneHouseBack)
        result = oneHouseBack

        twoHousesBack, oneHouseBack = 0, 0
        for i in nums[1:]: 
            twoHousesBack, oneHouseBack = oneHouseBack, max(twoHousesBack + i, oneHouseBack)
        return max(result, oneHouseBack)


class Solution2(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        prev = curr= 0
        for i in nums[1:]:
            curr, prev = max(prev+i,curr), curr
        
        maximum = curr
        prev = curr = 0
        for i in nums[:-1]:
            curr, prev = max(prev+i,curr), curr
        return max(maximum,curr)