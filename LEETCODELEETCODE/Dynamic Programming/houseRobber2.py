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
print(5==True)

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

class Solution3:
    def rob(self, nums):
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
 
        # DONT DO IT THIS WAY DO NOT DO NOT IT MESSES UP SHIT
        #Compare the methods with [1,3,1,3,100] to see how this
        #produces a bas result
        # prev = nums[1]
        # curr = nums[2]
        
        curr = prev = 0
        for i in range(1,len(nums)):
            curr, prev = max(nums[i] + prev, curr), curr
            
        prev2 = curr2 = 0
        for i in range(len(nums)-1):
            curr2, prev2 = max(nums[i] + prev2, curr2), curr2
            
        return max(curr,curr2)
            
import collections
class Solution99:
    def rob(self, nums):
        
        def rec(end,current,dic):

            if current < end: return 0

            # DO NOT USE THIS VERISON IT WILL FAIL BC 0 IN THE DEFAULTDICT IS ACTUALLY SIGNIFICANT
            # if not dic[current]: dic[current] = max(rec(end,current-1,dic), rec(end,current-2,dic) + nums[current])
            if current not in dic: dic[current] = max(rec(end,current-1,dic), rec(end,current-2,dic) + nums[current])

            return dic[current]

        
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
 
       
        dic = collections.defaultdict(int)
        dic2 = collections.defaultdict(int)

        
        return max(rec(1,len(nums)-1,dic),rec(0,len(nums)-2,dic2))
        
       
class Solution4:
    def rob(self, nums):
        
        def rec(end,current,dic):

            if current < end: return 0

            # DO NOT USE THIS VERISON IT WILL FAIL BC 0 IN THE DEFAULTDICT IS ACTUALLY SIGNIFICANT
            # if not dic[current]: dic[current] = max(rec(end,current-1,dic), rec(end,current-2,dic) + nums[current])
            if current-2 not in dic: dic[current-2] = rec(end,current-2,dic)
            if current-1 not in dic: dic[current-1] = rec(end,current-1,dic)

            
            return max(dic[current-1], dic[current-2] + nums[current])

        
        
        # BASE CASES
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
 
       
        dic = collections.defaultdict(int)
        dic2 = collections.defaultdict(int)

        
        return max(rec(1,len(nums)-1,dic),rec(0,len(nums)-2,dic2))
        