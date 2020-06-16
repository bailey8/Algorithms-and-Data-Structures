class Solution:
    
    def __init__(self):
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
     
    def longestIncreasingPath(self, matrix) -> int:
        
        def dfs(row,col):
            
            # IF WE HAVE FOUND THE LENGTH OF THE MAX PATH AT THIS CELL, THEN RETURN IT
            if (row,col) in visited: return visited[(row,col)]
            
            # THIS IS LIKE OUR BASE CASE. iF WE CAN REACH NO MORE CELLS FROM HERE, WE WILL STILL
            # HAVE A LENGHT OF 1 BC EVERY CELL ITSELF IS A PATH OF LENGTH 1
            maxSoFar = 1
            
            # STANDARD WAY TO ITERATE OVER DIRECTIONS
            for coords in self.directions:
                
                x,y = row + coords[0], col + coords[1]
                # CHEKC TO SEE IF THE NEXT CELL IS VALID
                if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= matrix[row][col]: continue
                
                # dfs(X,Y) + 1 IS JUST SAYING, "ADD 1 TO THE PATH LENGTH RETURNED TO YOU, BC THE ELEMENT YOU ARE ON COUNTS AS A PATH TOO"
                maxSoFar = max(maxSoFar , dfs(x,y)+1)
                     
            #UPDATE THE VISITED DICTIONARY TO REFLECT MAX LENGTH AT THIS CELL
            visited[row,col] = maxSoFar
            return maxSoFar

        
        # OUR "GLOBAL" MAXIMUM VARIABLE
        maximum = 0
        visited = {}
        
        # PERFORM DFS ON EVERY CELL IN THE MATRIX
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                maximum = max(dfs(row,col),maximum)
        return maximum
        
class Solution:
    
    def __init__(self):
        self.directions = [[1,0],[-1,0],[0,1],[0,-1]]
    def longestIncreasingPath(self, matrix) -> int:
        
        if not matrix: return 0
        
        max_ = 1
        
        def dfs(row,col,length):
            
            nonlocal max_
            max_ = max(max_, length)
 
            # search in all direcitons
            for direction in self.directions:
                x,y = row + direction[0], col + direction[1]
                
                if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] <= matrix[row][col]: continue
                dfs(x,y, length + 1)
        
        # SEARCH EVERY SINGLE CELL FOR LONGEST PATH             
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dfs(row,col,1)
        return max_

print(Solution().longestIncreasingPath([[1,2]]))

import collections
class Solution:
    
    def __init__(self):
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def longestIncreasingPath(self, matrix):
        # idea, use topological sort, search around to find the # of incoming nodes, start with zero indegree with queue, 
        # pop from queue, search around and reduce the indegree by 1; push to queue if indegree is 0. output the steps. Time O(mn) and Space O(mn).
        if not matrix: return 0
         
        inDegree = {}

        # FIND ALL THE INCOMING EDGES FOR EVERY CELL
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                incomingEdges = 0
                for dx, dy in self.directions:
                    x, y = row + dx, col + dy
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[row][col] > matrix[x][y]:
                        incomingEdges += 1
                inDegree[(row, col)] = incomingEdges # map point to the # of incoming degree
        
        # PERFROM TOP SORT, BUT KEEP TRACK OF THE "WAVES"
        queue = collections.deque([node for node in inDegree if not inDegree[node]])

        # bfs with queue, and update the step until queue is empty
        WAVE = 0
        while queue:
            batchSize = len(queue)
            for _ in range(batchSize):
                row, col = queue.popleft()
                #REMOVE AN INDEGREE FROM ALL THE OUTGOING EDGES!!!
                for dx, dy in self.directions:
                    x, y = row + dx, col + dy
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[row][col]:
                        inDegree[(x, y)] -= 1
                        # IF NO MORE INCOMING EDGES, THEN ADD IT TO THE QUEUE
                        if inDegree[(x, y)] == 0:
                            queue.append((x, y))
            WAVE += 1
        return WAVE


def longestIncreasingPath(self, matrix):
    
    
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    
    dp = [[0] * N for i in range(len(matrix))]
    return max(dfs(x, y) for x in range(len(matrix)) for y in range(matrix[0]))


a = [9]
b = [0]

if a[0]: print("hi") # YES
if b[0]: print("hi") # NO


