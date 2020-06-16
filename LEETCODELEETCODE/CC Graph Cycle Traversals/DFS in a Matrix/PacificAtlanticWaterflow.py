class Solution(object):

    def __init__(self):
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        rowLength, colLength = len(matrix),  len(matrix[0])
        pacificVisited = [[False] * colLength for _ in range(rowLength)]
        atlanticVisited = [[False] * colLength for _ in range(rowLength)]
        result = []
        
        # START DFS FOR THE FIRST AND LAST COLUMNS
        for row in range(rowLength):
            # FIRST COLUMN IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.dfs(matrix, row, 0, pacificVisited, rowLength, colLength)
            # LAST COLUMN IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.dfs(matrix, row, colLength-1, atlanticVisited, rowLength, colLength)

        # START DFS FOR THE FIRST AND LAST ROW
        for col in range(colLength):

            # TOP ROW IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.dfs(matrix, 0, col, pacificVisited, rowLength, colLength)
            # BOOT ROW IS THE ATLANTIC, SO PASS IN THE ATLANTIC VISITED SET
            self.dfs(matrix, rowLength-1, col, atlanticVisited, rowLength, colLength)
            
        for i in range(rowLength):
            for j in range(colLength):
                if pacificVisited[i][j] and atlanticVisited[i][j]:
                    result.append([i,j])
        return result
                
                
    def dfs(self, matrix, i, j, visited, m, n):
       
    # MARK THE CELL AS VISITED
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            
            # THIS IS A BOUNDS CHECK, IT ALSO CHECKS IF WE HAVE VISITED THE NEW CELL, AND IT CHECKS IF IT IS VALID WATER LEVEL
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)

# Using a set
class Solution2(object):

    def __init__(self):
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]


    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        rowLength, colLength = len(matrix), len(matrix[0])

        # THE CELLS WE CAN REACH FROM THE TOP AND LEFT SIDES OF MATRIX
        pacificVisited = set()
        # THE CELLS WE CAN REACH FROM THE BOTTOM AND RIGHT SIDES OF THE MATRIX
        atlanticVisited = set()
        
        # START DFS FOR THE FIRST AND LAST COLUMNS
        for row in range(rowLength):
            # FIRST COLUMN IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.dfs(matrix, row, 0, pacificVisited, rowLength, colLength)
            # LAST COLUMN IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.dfs(matrix, row, colLength-1, atlanticVisited, rowLength, colLength)

        # START DFS FOR THE FIRST AND LAST ROW
        for col in range(colLength):

            # TOP ROW IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.dfs(matrix, 0, col, pacificVisited, rowLength, colLength)
            # BOOT ROW IS THE ATLANTIC, SO PASS IN THE ATLANTIC VISITED SET
            self.dfs(matrix, rowLength-1, col, atlanticVisited, rowLength, colLength)
            
        #RETURN THE CELLS THAT WE COULD REACH FROM BOTH THE PACIFIC AND ALANTIC
        return [list(coord) for coord in atlanticVisited.intersection(pacificVisited)]
                
                
    def dfs(self, matrix, row, col, visited, rowLength, colLength):
        # when dfs called, meaning its caller already verified this point 
        visited.add((row,col))
        for dir in self.directions:
            x, y = row + dir[0], col + dir[1]

            # CHECK IF NEW INDEX IS IN BOUNDS
            if x < 0 or x >= rowLength or y < 0 or y >= colLength: continue
            # CHECK IF NEW INDEX IS IN CACHE OR IF WE VISITED IT
            if (x,y) in visited: continue
            # CHECK IF NEW INDEX IS VALID TO VISIT
            if matrix[x][y] < matrix[row][col]: continue
            self.dfs(matrix, x, y, visited, rowLength, colLength)




################# BFS
import collections
class Solution99(object):

    def __init__(self):
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        rowLength, colLength = len(matrix),  len(matrix[0])
        pacificVisited = [[False] * colLength for _ in range(rowLength)]
        atlanticVisited = [[False] * colLength for _ in range(rowLength)]
        result = []
        
        # START DFS FOR THE FIRST AND LAST COLUMNS
        for row in range(rowLength):
            # FIRST COLUMN IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.bfs(matrix, row, 0, pacificVisited, rowLength, colLength)
            # LAST COLUMN IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.bfs(matrix, row, colLength-1, atlanticVisited, rowLength, colLength)

        # START DFS FOR THE FIRST AND LAST ROW
        for col in range(colLength):

            # TOP ROW IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.bfs(matrix, 0, col, pacificVisited, rowLength, colLength)
            # BOOT ROW IS THE ATLANTIC, SO PASS IN THE ATLANTIC VISITED SET
            self.bfs(matrix, rowLength-1, col, atlanticVisited, rowLength, colLength)
            
        for i in range(rowLength):
            for j in range(colLength):
                if pacificVisited[i][j] and atlanticVisited[i][j]:
                    result.append([i,j])
        return result
                
                
    def bfs(self, matrix, i, j, visited, m, n):
        if visited[i][j]: return 
        queue = collections.deque([(i,j)])
        while queue:
            i, j = queue.popleft()
            visited[i][j] = True
            for dir in self.directions:
                x, y = i + dir[0], j + dir[1]
            
                # THIS IS A BOUNDS CHECK, IT ALSO CHECKS IF WE HAVE VISITED THE NEW CELL, AND IT CHECKS IF IT IS VALID WATER LEVEL
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]: continue
                queue.append((x,y))



# DFS WITH STACK
class Solution7(object):

    def __init__(self):
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        rowLength, colLength = len(matrix),  len(matrix[0])
        pacificVisited = [[False] * colLength for _ in range(rowLength)]
        atlanticVisited = [[False] * colLength for _ in range(rowLength)]
        result = []
        
        # START DFS FOR THE FIRST AND LAST COLUMNS
        for row in range(rowLength):
            # FIRST COLUMN IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.bfs(matrix, row, 0, pacificVisited, rowLength, colLength)
            # LAST COLUMN IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.bfs(matrix, row, colLength-1, atlanticVisited, rowLength, colLength)

        # START DFS FOR THE FIRST AND LAST ROW
        for col in range(colLength):

            # TOP ROW IS PACIFIC OCEAN, SO PASS IN THE PACIFIFC VISITED SET
            self.bfs(matrix, 0, col, pacificVisited, rowLength, colLength)
            # BOOT ROW IS THE ATLANTIC, SO PASS IN THE ATLANTIC VISITED SET
            self.bfs(matrix, rowLength-1, col, atlanticVisited, rowLength, colLength)
            
        for i in range(rowLength):
            for j in range(colLength):
                if pacificVisited[i][j] and atlanticVisited[i][j]:
                    result.append([i,j])
        return result
                
                
    def bfs(self, matrix, i, j, visited, m, n):
        if visited[i][j]: return 
        stack = [(i,j)]
        while stack:
            i, j = stack.pop()
            visited[i][j] = True
            for dir in self.directions:
                x, y = i + dir[0], j + dir[1]
            
                # THIS IS A BOUNDS CHECK, IT ALSO CHECKS IF WE HAVE VISITED THE NEW CELL, AND IT CHECKS IF IT IS VALID WATER LEVEL
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]: continue
                stack.append((x,y))