# COIN CHANGE 2 - O(AMOUNT*LEN(NUMS)) SPACE
class Solution:
    def change(self, amount: int, coins) -> int:

        # Each row represents using the denominations up to that point in the denominations array (see the video explanation)
        cache = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]

        # Max ways to make change for 0 will be 1, doing nothing. THE REST OF THE FIRST ROW IS 0 BC WITH NO COINS YOU CANT DO SHIT
        # EXCEPT YOU CAN MAKE CHANGE FOR AMOUNT 0 WITH 0 COINS, SO THATS WHY WE HAVE THIS EXCEPTION 
        cache[0][0] = 1

        for row in range(1,len(coins)+1):
            
            cache[row][0] = 1 # THERE IS 1 WAY TO MAKE CHANGE FOR AMOUNT 0 (JUST GIVE THEM NOTHING)

            for col in range(1,amount+1):

                #THIS IS THE ROW IN OUR DP TABLE. THIS IS THE ROW IN OUR DP TABLE            
                currentCoinValue = coins[row-1]

                """
                dp[i][j] will be the sum of the ways to make change not considering
                this coin (dp[i-1][j]) and the ways to make change considering this
                coin (dp[i][j] - currentCoinValue] ONLY if currentCoinValue <= j, otherwise
                this coin can not contribute to the total # of ways to make change at this
                sub problem target amount)
                """
                # IF WE CHOOSE NOT TO USE THE COIN, THEN KEEP THE TARGET VALUE THE SAME, AND COSIDER ALL COINS BUT THE COIN WE ARE ON (ROW-1)
                withoutThisCoin = cache[row-1][col]
                # IF OUR TARGET AMOUNT IS LESS THAN THE VALUE OF OUR COIN, THEN WE CANT USE IT
                # IF IT IS NOT, THEN SUBTRACT THE VALUE OF IT FROM THE TARGET (COL - CURRENTCOIVALUE)
                withThisCoin = cache[row][col - currentCoinValue] if currentCoinValue <= col else 0

                # ADD THE TWO TOGETHER
                cache[row][col] = withoutThisCoin + withThisCoin

        """
        The answer considering ALL coins for the FULL amount is what
        we want to return as the answer
        """
        return cache[len(coins)][amount]




class Solution:
    def change(self, amount: int, coins) -> int:
        # Each row represents using the denominations up to that point in the denominations array (see the video explanation)

        cache = [0 for _ in range(amount+1)] 
        
        # Max ways to make change for 0 will be 1, doing nothing. THE REST OF THE FIRST ROW IS 0 BC WITH NO COINS YOU CANT DO SHIT
        # EXCEPT YOU CAN MAKE CHANGE FOR AMOUNT 0 WITH 0 COINS, SO THATS WHY WE HAVE THIS EXCEPTION 
        cache[0] = 1

        for coinIndex in range(1,len(coins)+1):
            for amountIndex in range(amount+1):
                
                #THIS IS THE ROW IN OUR DP TABLE. THIS IS THE ROW IN OUR DP TABLE            
                currentCoinValue = coins[coinIndex-1]
               
                # SAME TARGET AMOUNT, BUT CONSIDER 1 LESS COIN
                withoutThisCoin = cache[amountIndex]

                # SUBTRACT COIN VALUE FROM AMOUNT AND STILL CONSIDER ALL THE COINS
                withThisCoin = cache[amountIndex - currentCoinValue] if currentCoinValue <= amountIndex else 0

                # ADD THE TWO TOGETHER
                cache[amountIndex] = withoutThisCoin + withThisCoin

        # The answer considering ALL coins for the FULL amount is what we want to return as the answer
        return cache[-1]




class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def changeWays(amountLeft, coinIndex):

            # If the amount is equal to 0, then return 1, because we successfully made change
            if amountLeft == 0: return 1

            # IF WE USE TOO MUCH CHANGE OR USE ALL OUR COINS
            if amountLeft <= 0 or coinIndex == -1: return 0

            if ways[coinIndex][amountLeft] == -1: ways[coinIndex][amountLeft] = changeWays(amountLeft-coins[coinIndex], coinIndex) + changeWays(amountLeft, coinIndex - 1)


            return ways[coinIndex][amountLeft]
            
        ways = [ [-1 for _ in range(amount+1)] for _ in range(len(coins))]
        return changeWays(amount, len(coins)-1)


