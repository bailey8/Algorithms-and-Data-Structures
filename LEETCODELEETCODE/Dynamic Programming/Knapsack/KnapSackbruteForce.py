

def solve_knapsack(profits, weights, capacity):
  
    def knapsack_recursive(capacity, currentIndex):
    
        # BOUNDING FUNCTION. IF WE EXCEED OUR WEIGHT OR EXAUST THE VALUES, THEN RETURN 0
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        # recursive call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
        profit1 = 0

        # ------------------ WE EITHER USE THE VALUE OR WE DONT ----------------------------------------#
        # IF WE USE THIS ELEMENT, THEN ADD ITS VALUE, AND SUBTRACT ITS WEIGHT
        if weights[currentIndex] <= capacity: 
            profit1 = profits[currentIndex] + knapsack_recursive(capacity - weights[currentIndex], currentIndex + 1) #USE VALUE

        #IF WE DONT INCLUDE THIS ELEMENT, THEN IGNORE THE WEIGHT, AND IGNORE THE VALUE
        profit2 = knapsack_recursive(capacity, currentIndex + 1)                                                    # DONT USE VALUE

        return max(profit1, profit2)

    return knapsack_recursive(capacity, 0)

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()