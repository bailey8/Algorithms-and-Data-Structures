# Find recursive relation
# rob(i) = max( rob(i - 2) + currentHouseValue, rob(i - 1) )


# Recursive (top-down)
#top down so I am starting from end of list
def robNaive(arr):
    return robHelper(arr,len(arr)-1)
def robHelper(arr,i):
    if i < 0:
        return 0
    return max(robHelper(arr,i-1),robHelper(arr,i-2)+arr[i])

print(robNaive([1,2,3,1]))
print(robNaive([2,7,9,3,1]))

# Recursive + memo (top-down)
# Must use array because we have to track inde
# memo = {}
memo = []
def robMemo(list):
    global memo
    memo = [-1]*len(list)
    return robMemoHelper(list,len(list)-1)
def robMemoHelper(list,i):
    if i < 0:
        return 0
    if memo[i-1] < 0: memo[i-1] = robMemoHelper(list,i-1)
    if memo[i-2] < 0: memo[i-2] = robMemoHelper(list,i-2)
    # if (i-1) not in memo: memo[i-1] = robMemoHelper(list,i-1)
    # if (i-2) not in memo: memo[i-2] = robMemoHelper(list,i-2)
    return max(memo[i-1],memo[i-2]+list[i])

print(robMemo([1,2,3,1]))
print(robMemo([2,7,9,3,1]))

# Iterative + memo (bottom-up)
def dp(list):
    # Always check for edge case
    if len(list) ==0: return 0
    prev2 = 0
    prev1 = 0
    for money in list:
        temp = prev1
        prev1 = max(prev1,prev2+money)
        prev2 = temp
    return prev1

print(dp([1,2,3,1]))
print(dp([2,7,9,3,1]))
# Iterative + N variables (bottom-up)