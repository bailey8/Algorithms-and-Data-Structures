# Recurrance Relation : uniquePaths(m,n) = uniquePaths(m-1,n) + uniquePaths(m,n-1)

# Idea is to work back recursivley until the base case, and then take the sum of the unique paths from left and right
def uniquePaths(n,m):
    if m ==1 or n ==1:
        return 1
    right = uniquePaths(n,m-1)
    left = uniquePaths(m,n-1)
    return left + right

dic = {}
def uniquePathsMemo(n,m):
    if m == 1 or n==1:
        return 1
    if (n-1,m) not in dic: dic[(n-1,m)] = uniquePaths(n-1,m)
    if (n,m-1) not in dic: dic[(n,m-1)] = uniquePaths(n,m-1)

    return dic[(n-1,m)] + dic[(n,m-1)]

class Solution(object):
    def uniquePaths(self, n, m):
        list = [[0]*m for i in range(n)]
        for i in range(n):
            list[i][0] = 1
        for j in range(m):
            list[0][j] = 1
        # For each row, go through column by column
        for i in range(1,m):
            for j in range(1,m):
                list[i][j] = list[i-1][j] + list[i][j-1]
        return list[-1][-1]
         