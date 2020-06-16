class Solution(object):
    def threeSumSmaller(self, nums,target):

        nums.sort()
        count = 0

        for i in range(len(nums) -2):

            left = i+1
            right = len(nums)-1
            
            while left < right:
                
                if nums[left] + nums[right] + nums[i] < target:
                    
                    # for i in range(right, left, -1):
                    #     triplets.append([arr[first], arr[left], arr[i]])

                    # THIS LINE IS THE KEY. THIS LINE IS THE KEY. THIS LINE IS THE KEY
                    count += right - left
                    left += 1
                
                # IF THE SUM IS TOO BIG, THEN SHRINK IT. SINCE ARRAY IS IN SORTED ORDER WE JUST DECREMENT THE LEFT POINTER
                else: right -= 1

        return count
