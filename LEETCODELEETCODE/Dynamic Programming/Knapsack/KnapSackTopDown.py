
# def solve_knapsack(profits, weights, capacity):

#     def knapsack_recursive(capacity, currentIndex):

#         # BOUNDING FUNCTION
#         if capacity <= 0 or currentIndex >= len(profits): return 0

#         # IF WE HAVE SOLVED SIMILIAR PROBLEM, RETRIVE IT FROM THE CACHE
#         if CACHE[currentIndex][capacity] != -1: return CACHE[currentIndex][capacity]

#         # recursive call after choosing the element at the currentIndex
#         # if the weight of the element at currentIndex exceeds the capacity, we
#         # shouldn't process this
#         profit1 = 0
#         if weights[currentIndex] <= capacity:
#             profit1 = profits[currentIndex] + knapsack_recursive(capacity - weights[currentIndex], currentIndex + 1)

#         # recursive call after excluding the element at the currentIndex
#         profit2 = knapsack_recursive(capacity, currentIndex + 1)

#         CACHE[currentIndex][capacity] = max(profit1, profit2)
#         return CACHE[currentIndex][capacity]

#     # create a two dimensional array for Memoization, each element is initialized to '-1'
#     CACHE = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
#     return knapsack_recursive( capacity, 0)


#Better Verison
def solve_knapsack(profits, weights, capacity):

    def knapsack_recursive(capacity, currentIndex):

        # BOUNDING FUNCTION
        if capacity <= 0 or currentIndex == -1: return 0

        # IF WE HAVE SOLVED SIMILIAR PROBLEM, RETRIVE IT FROM THE CACHE
        if CACHE[currentIndex][capacity] != -1: return CACHE[currentIndex][capacity]

        # recursive call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity, we
        # shouldn't process this
        profit1 = 0
        if weights[currentIndex] <= capacity: profit1 = profits[currentIndex] + knapsack_recursive(capacity - weights[currentIndex], currentIndex - 1)

        # recursive call after excluding the element at the currentIndex
        profit2 = knapsack_recursive(capacity, currentIndex - 1)

        CACHE[currentIndex][capacity] = max(profit1, profit2)
        return CACHE[currentIndex][capacity]

    # create a two dimensional array for Memoization, each element is initialized to '-1'
    CACHE = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(capacity, len(profits)-1)

print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
