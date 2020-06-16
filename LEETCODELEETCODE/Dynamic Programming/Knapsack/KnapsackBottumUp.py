
def solve_knapsack(profits, weights, capacity):

    if capacity <= 0 or not profits or len(weights) != len(profits): return 0

    # THE ROWS ARE THE PROFITS - THIS IS IDENTICAL TO THE SUBSET SUM PROBLEM. THIS
    cache = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for row in cache: row[0] = 0

    # MANUALLY FILL OUT THE FIRST ROW.
    for column in range(capacity+1):
        if weights[0] <= column:
            cache[0][column] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, len(cache)):
        for c in range(1, len(cache[0])):
            profit1, profit2 = 0, 0

            # include the item, if it is not more than the capacity
            if weights[i] <= c: profit1 = profits[i] + cache[i - 1][c - weights[i]]

            # exclude the item
            profit2 = cache[i - 1][c]

            # take maximum
            cache[i][c] = max(profit1, profit2)

    # maximum profit will be at the bottom-right corner.
    return cache[-1][-1]

# GOOD, CLEAN VERSION
def solve_knapsack(profits, weights, capacity):

    # cache = [[0 for _ in range(capacity+1)] for _ in range(len(profits)+1)]

    # for row in range(len(cache)):
    #     profit, weight = profits[row-1], weights[row-1]

    #     for col in range(len(cache[0])):
    #         profit1 = profit2 = 0
    #         # include the item, if it is not more than the capacity
    #         if weight <= col: profit1 = cache[row-1][col-weight] + profit
    #         # exclude the item
    #         profit2 = cache[row-1][col]
    #         # take maximum
    #         cache[row][col] = max(profit1,profit2)

    # return cache[-1][-1]

    cache = [[0 for _ in range(capacity+1)] for _ in range(len(profits)+1)]

    for row in range(1, len(cache)):
        weight = weights[row-1]
        for col in range(1, len(cache[0])):

            if weight <= col: cache[row][col] = max(cache[row-1][col], cache[row-1][col-weight] + profits[row-1])
            else: cache[row][col] = cache[row-1][col]

    return cache[-1][-1]


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))



# def solve_knapsack(profits, weights, capacity):
#   # basic checks
#   n = len(profits)
#   if capacity <= 0 or n == 0 or len(weights) != n:
#     return 0

#   dp = [0 for x in range(capacity+1)]

#   # if we have only one weight, we will take it if it is not more than the capacity
#   for c in range(0, capacity+1):
#     if weights[0] <= c:
#       dp[c] = profits[0]

#   # process all sub-arrays for all the capacities
#   for i in range(1, n):
#     for c in range(capacity, -1, -1):
#       profit1, profit2 = 0, 0
#       # include the item, if it is not more than the capacity
#       if weights[i] <= c:
#         profit1 = profits[i] + dp[c - weights[i]]
#       # exclude the item
#       profit2 = dp[c]
#       # take maximum
#       dp[c] = max(profit1, profit2)

#   return dp[capacity]


# def main():
#   print("Total knapsack profit: " +
#         str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
#   print("Total knapsack profit: " +
#         str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


# main()


b = [1,2,2,3,4]
c = [5 if a==1 elif a==2 6 else 3 for ]