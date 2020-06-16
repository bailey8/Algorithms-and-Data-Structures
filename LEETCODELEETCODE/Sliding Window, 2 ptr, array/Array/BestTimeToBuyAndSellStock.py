class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # TRACK THE SMALLEST ELEMENT
        small = float('inf')
        
        # THIS IS THE LARGEST ELEMENT WE HAVE IN OUR WINDOW
        large = 0
        
        # THE BEST PROFIT WE HAVE MADE SO FAR
        maximum = 0
        
        # FOR EVERY STOCK IN THE PRICES
        for stock in prices:
            
            #IF THIS STOCK HAS A SMALLER BUY PRICE THAN THE PREVOUS ONE, THEN WE WANT TO USE IT
            if stock < small:
                small = stock
                # WE NEED TO RESET OUR LARGEST VALUE, BECAUSE NOW WE SHIFTED OUR WINDOW TO THE RIGHT, SO 
                # THE PREVIOUS LARGEST VALUE WOULD BE BEFORE THIS NEW WINDOW STARTS, WHICH IS ILLEGAL
                large = float('-inf')
                
            #IF WE HAVE A NEW LARGEST VALUE, THEN THE FIX IS SIMPLE, JUST UPDATE OUR LARGEST VALUE
            elif stock > large:
                large = stock
        
                # check if the new large value - small (purchase price) value gets you a greater profit than your previous window
                maximum = max(large - small,maximum)
        return maximum
                

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
  
        minPRICEsoFar, maxPROFITsoFar = float('inf'), 0
        
        for i in range(len(prices)):
            
            # UPDATE MIN PRICE IF NEEDED
            if minPRICEsoFar > prices[i]:
                minPRICEsoFar = prices[i]
                
            else:
                # the max is either the prev max or our current stock price - price we bought it for
                maxPROFITsoFar =  max(maxPROFITsoFar, prices[i] - minPRICEsoFar);
        
        return maxPROFITsoFar      
        