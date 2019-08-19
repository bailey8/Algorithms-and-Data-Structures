# class Solution(object):
def numIslands(self, grid):

    def search(r,c):
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])): return False
        # visited.add((r,c))
        visited.add((r,c))
        if grid[r][c] == "0": return False
        if (r+1,c) not in visited: search(r+1,c)
        if (r,c+1) not in visited: search(r,c+1)
        if (r,c-1) not in visited: search(r,c-1)
        if (r-1,c) not in visited: search(r-1,c)


        
    visited = set()
    count = 0
    for r,row in enumerate(grid):
        for c,elem in enumerate(row):
            if elem == "1" and (r,c) not in visited:
                search(r,c)
                count +=1
    return count

class Solution2(object):
    def numIslands(self, grid):

        def search(r,c):
            if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])): return False
            if grid[r][c] == "0": return False
            grid[r][c] = "0"
            search(r+1,c)
            search(r,c+1)
            search(r,c-1)
            search(r-1,c)

 
            
        count = 0
        for r,row in enumerate(grid):
            for c,elem in enumerate(row):
                if elem == "1":
                    search(r,c)
                    count +=1
        return count
                                 
                