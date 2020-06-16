

class Solution:
    def numIslands(self, grid):
        
        
        def explore(row,col):
            
            #CHECK IF THE BOUNDS ARE OKAY
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            
            #CHECK IF WE HIT WATER OR IF THE LAND CELL WAS VISITED
            if grid[row][col] == "0":
                return
            
            # MARK THE LAND CELL AS VISITED
            grid[row][col] = "0"
            
            explore(row+1,col)
            explore(row-1,col)
            explore(row,col+1)
            explore(row,col-1)
        
        # WE START WITH NO ISLANDS
        numberOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                # THIS DENOTES AN UNVISITED ISLAND
                if grid[i][j] == "1":
                    numberOfIslands += 1
                    
                    #THIS FUNCITON CONVERTS EVERY "1" IN THE ISLAND TO "#" SO WE KNOW WE VISITED IT
                    explore(i,j)
        
        return numberOfIslands
        
import collections
class Solution2:
    def numIslands(self, grid):
        
        
        def bfs(row,col):
            
            queue = collections.deque([(row,col)])
            
            while queue:
                row,col = queue.popleft()
                
                #CHECK IF THE BOUNDS ARE OKAY
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): continue
            
                #CHECK IF WE HIT WATER
                if grid[row][col] == "0": continue

                #CHECK IF WE ALREADY VISITED THE LAND CELL
                grid[row][col] = "0"
            
                queue.append((row+1,col))
                queue.append((row-1,col))
                queue.append((row,col+1))
                queue.append((row,col-1))
        
        # WE START WITH NO ISLANDS
        numberOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                # THIS DENOTES AN UNVISITED ISLAND
                if grid[i][j] == "1":
                    numberOfIslands += 1
                    
                    #THIS FUNCITON CONVERTS EVERY "1" IN THE ISLAND TO "#" SO WE KNOW WE VISITED IT
                    bfs(i,j)
                        
        return numberOfIslands


class Solution6:
    
    def __init__(self):
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    def numIslands(self, grid):
        
        def dfs(row,col):
            
            # NOW THAT WE HAVE VISITED THE SQUARE, SET IT TO WATER SO WE DONT CALL DFS ON IT AGAIN
            grid[row][col] = "0"
            
            # EXPLORE ALL VALID DIRECTIONS
            for direction in self.directions:
                x,y = row + direction[0], col + direction[1]
                # ONLY EXPLORE LAND CELLS THAT ARE IN BOUNDS
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0": continue
                # CALL DFS ON THE VALID CELLS
                dfs(x,y)
                
        #CALL DFS ON EVERY LAND CELL
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row,col)
        return count
        
        
            
        
        
        
        
        
        
        
    
                