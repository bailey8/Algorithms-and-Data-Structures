class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        count = 0
        
        windowSTART = 0
        windowTotal = 0
        
        for windowEND, cals in enumerate(calories):
            
            # UPDATE THE CALS BC WE INCLUDE ANOTHER ELEMENT
            windowTotal += cals
            
            # IF THIS IS A VALID WINDOW, THEN CHECK THE WINDOW SUM AND ASSESS WHETHER
            # IT IS GOOD OR BAD
            if windowEND - windowSTART + 1 == k:
                
                if windowTotal < lower: count -= 1
                if windowTotal > upper: count += 1
                    
                # THIS IS THE KEY. THIS MUST BE DONE AFTER AFTER AFTER WE ASSESS (PREP FOR NEXT WINDOW)
                windowTotal -= calories[windowSTART]
                windowSTART += 1     
                
        return count
                
                