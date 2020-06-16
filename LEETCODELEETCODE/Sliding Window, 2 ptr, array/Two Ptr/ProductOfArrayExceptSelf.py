class Solution:
    def productExceptSelf(self, nums):
        
        # The left and right arrays as described in the algorithm
        productToLeft, productToRight, answer = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        
        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        productToLeft[0] = 1
        for i in range(1, len(nums)):
            
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            productToLeft[i] = nums[i - 1] * productToLeft[i - 1]
        
        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1. SET LAST ELEMENT TO 1 BC NO ELEMENTS TO THE RIGHT OF LAST ELEMENT
        productToRight[-1] = 1
        for i in reversed(range(len(nums))):
            
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # SIMPLY MULTIPLYING it with nums[i + 1] would give the product of all 
            # elements to the right of index 'i'
            productToRight[i] = nums[i + 1] * productToRight[i + 1]
        
        # Constructing the answer array
        for i in range(len(nums)):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = productToLeft[i] * productToRight[i]
        
        return answer


class Solution2:
    def productExceptSelf(self, nums):
           
        # The answer array to be returned
        leftCache = [1]*len(nums)
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        leftCache[0] = 1

        for i in range(1, len(nums)):
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            leftCache[i] = nums[i - 1] * leftCache[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        productToRight = 1
        for i in reversed(range(len(nums))):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            # RN OUR ANSWER ARRAY HAS THE PRODUCT OF ALL ELEMENTS TO THE LEFT OF EACH INDEX
            # WE NOW KEEP A TEMP "ACCUMULATOR" VARIABLE THAT TRACKS THE CURRENT PRODUCT OF ALL NUMS TO THE 
            #RIGHT OF THE INDEX IN ORIGINAL ARRAY
            leftCache[i] = leftCache[i] * productToRight
            productToRight *= nums[i]
        
        return leftCache


class Solution4(object):
    def productExceptSelf(self, nums):
        
        temp = [1] * len(nums)

        #identity multiplication values
        left_value = 1
        right_value = 1

        # OUR TWO POINTERS
        left_index = 0
        right_index = len(nums)-1

        for value in range(len(nums)):
            # LEFT INDEX WILL BE MULTIPLIED EVERYTHING TO THE LEFT (FIRST ITERATION THIS IS 1 BC THERE IS NOTHING TO LEFT)
            # THIS IS WHY WE START BY HAVING THE IDENTITY AS 1, BC EVERYTHING TO THE LEFT OF 0TH INDEX IS 1
            temp[left_index] *= left_value #multiply by everything that is to left
            #SAME CONCEPT FOR THE RIGHT INDEX
            temp[right_index] *= right_value #Multiply by everything that is to right
            
            # Update the product of elements to the left AFTER (AFTER) AFTER you modify the temp array (we dont want to include the element itself in the product)
            # remember we only care about the elemnts themselves
            left_value *= nums[left_index]
            right_value *= nums[right_index]
            
            #adjust indices as needed
            left_index+=1
            right_index-=1

        return temp




class Solution2:
    def productExceptSelf(self, nums):
           
        cache = [1]*len(nums)
    
        for leftPtr in range(1, len(nums)):
            cache[leftPtr] = nums[leftPtr - 1] * cache[leftPtr - 1]
        
        rightCache = 1
        for rightPtr in reversed(range(len(nums))):
            
            # rightCache does not include the current element - we add current element AFTER this call
            cache[rightPtr] = cache[rightPtr] * rightCache
            rightCache *= nums[rightPtr]
        
        return cache