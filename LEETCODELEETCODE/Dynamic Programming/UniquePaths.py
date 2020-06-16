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


# THIS IS THE ALTERNATIVE WAY TO DO THE INDEXING
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


         
# THIS IS THE BACKWARDS WAY TO DO THE INDEXING
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 0 or n == 0: return 0
        
        numberOfPaths = [[0 for _ in range(n)] for _ in range(m)]
        
        
        # POPULATE THE BASE CASES
        # 1 1 1
        # 1 0 0
        # 1 0 0
        for x_cord in range(m):
            numberOfPaths[x_cord][0] = 1
        for y_cord in range(n):
            numberOfPaths[0][y_cord] = 1
    
        # ADD UP THE PATHS OF THE PREVIUS CELLS
        # 1 1 1
        # 1 2 3
        # 1 3 6
        for x_cord in range(1,m):
            for y_cord in range(1,n):
                numberOfPaths[x_cord][y_cord] =numberOfPaths[x_cord-1][y_cord] + numberOfPaths[x_cord][y_cord-1]
        
        # return the bottom right cell
        return numberOfPaths[-1][-1]
                

# I DO NOT RECCOMMENT THE INDEXING BELOW
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 0 or n == 0: return 0
        
        numberOfPaths = [[0 for _ in range(n)] for _ in range(m)]
        numberOfPaths[0][0] = 1
        
        
        def helper(x,y):
             
            # Just return 1 if they are near the edges
            # 1 1 1
            # 1 0 0
            # 1 0 0
            if x == 0 or y == 0: return 1
            
            if not numberOfPaths[x-1][y]: numberOfPaths[x-1][y] = helper(x-1,y)
            if not numberOfPaths[x][y-1]: numberOfPaths[x][y-1] = helper(x,y-1)
            
            return numberOfPaths[x-1][y] + numberOfPaths[x][y-1]
            
        
        return helper(m-1,n-1)

            
            

            
            
                
        