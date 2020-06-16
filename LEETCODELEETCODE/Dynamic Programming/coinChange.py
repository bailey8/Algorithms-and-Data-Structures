class Solution:
    def coinChange(self, coins, amount: int) -> int:
        
        def dfs(amountLeft):
            
            if amountLeft == 0: return 0          
            if amountLeft < 0: return float('inf')
            if amountLeft in cache: return cache[amountLeft]
            
            fewestCoinsNeeded = float('inf')
            for coin in coins:
                count =  dfs(amountLeft - coin) + 1
                fewestCoinsNeeded = min(fewestCoinsNeeded,count)
                
            cache[amountLeft] = fewestCoinsNeeded
            return cache[amountLeft]
        
        cache = {}
        
        dfs(amount)
        if amount < 1: return 0
        return -1 if cache[amount] == float('inf') else cache[amount]

class Solution8:
    def coinChange(self, coins, amount: int) -> int:
        
        cache = [float('inf')] * (amount + 1)
        # 0 COINS NEEDED TO MAKE CHANGE FOR AMOUNT 0
        cache[0] = 0
        
        # Solve every subproblem from 1 to amount
        for index in range(1,amount+1):
            for coin in coins:
                
                # IF SUBTRACTING THIS COIN IS NOT LESS THAN 0, EXPLORE IT
                if index-coin >= 0: cache[index] = min(cache[index], cache[index - coin] + 1)
                    
        return cache[amount] if cache[amount] != float('inf') else -1 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = [float('inf')] * (amount + 1)

        # ZERO COINS NEEDED TO MAKE CHANGE AMOUNT 0
        cache[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                cache[x] = min(cache[x], cache[x - coin] + 1)
        return cache[amount] if cache[amount] != float('inf') else -1 

        
  
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        
        if amount < 1: return 0
        cache = [[float('inf') for _ in range(amount+1)] for _ in range(len(coins)+1)]
        
        for row in cache: row[0] = 0
        
        # FOR EVERY COIN IN THE CACHE
        for coinIndex in range(1, len(cache)):
            coinValue = coins[coinIndex-1]
            for col in range(1,len(cache[0])):

                # Decide which one of the following solutions is the best:
                # 1. Using the previous solution for making remainder (without using current coin).
                # 2. Using the previous solution for making remainder - current coin value plus 1 extra coin
                if coinValue <= col: 
                    cache[coinIndex][col] = min(1+cache[coinIndex][col-coinValue], cache[coinIndex-1][col])

                # We cannot use this coin, so just use the previous solution
                else: cache[coinIndex][col] = cache[coinIndex-1][col]
           
        return -1 if cache[-1][-1] == float('inf') else cache[-1][-1]


