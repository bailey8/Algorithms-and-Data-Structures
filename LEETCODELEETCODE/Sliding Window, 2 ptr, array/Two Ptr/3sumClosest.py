class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums)-2):
            
            if i> 0 and nums[i] == nums[i-1]: continue
            
            left, right = i+1, len(nums) -1
                         
            while left < right:
                
                target_diff = target - nums[i] - nums[left] - nums[right]
                                 
                if abs(target_diff) < abs(closest): closest = target_diff
                
                if target_diff > 0: left += 1
                elif target_diff < 0: right -= 1
                else: return target
                 
        return target - closest
                        