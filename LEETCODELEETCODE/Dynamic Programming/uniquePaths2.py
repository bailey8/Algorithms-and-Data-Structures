class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be no paths to the destination.
        if obstacleGrid[0][0] == 1: return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        blocked = False
        # FOR EVERY ROW, ADD 1 TO THE POSSIBLE PATHS, BC THERE IS 1 WAY TO GO THERE
        for row in range(1,m):
            # IF NO OBSTACLE, THEN ADD 1
            if obstacleGrid[row][0] == 0 and not blocked: obstacleGrid[row][0] = 1
            #IF THERE IS AN OBSTACLE, THEN SET THE CELL TO 0 BC NO PATHS TO GET THERE (DUH ITS BLOCKED)
            # ALSO TRIGGER THE FLAG BC WE WILL NOT BE ABLE TO ACCESS CELLS TO THE RIGHT EITHER
            else: 
                obstacleGrid[row][0] = 0
                blocked = True

        # SAME CONCEPT AS ABOVE
        blocked = False
        for col in range(1, n):
            if obstacleGrid[0][col] == 0 and not blocked: obstacleGrid[0][col] = 1
            else:
                obstacleGrid[0][col] = 0
                blocked = True
             

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for row in range(1,m):
            for col in range(1,n):

                # IF THE CELL WAS ALREADY 1, THEN THERE IS WAS AN OBSTACLE
                if obstacleGrid[row][col]: obstacleGrid[row][col] = 0
                else: obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[-1][-1]