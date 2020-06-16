import math
class Solution:
    def solveSudoku(self, board):

        def canPlaceValue(row, col, charToPlace):
            #Check column of the placement
            for row_ in board:
                if charToPlace == row_[col]:
                    return False

            #Check row of the placement
            for i in range(len(board[0])):
                if charToPlace == board[row][i]:
                    return False

            # Check region constraints - get the size of the sub-box
            regionSize = int(math.sqrt(len(board))) # 9

            # THIS IS THE QUADRANT WE ARE IN
            verticalBoxIndex  = int(row / regionSize) # row = 5, row/regionSize = 1         (1,2)
            horizontalBoxIndex  = int(col / regionSize) # col = 6, col/regionSize = 2

            # THIS GIVES US THE TOP LEFT COORD OF OUR QUADRANT
            topLeftOfSubBoxRow = regionSize * verticalBoxIndex  # 3* 1 = 3
            topLeftOfSubBoxCol = regionSize * horizontalBoxIndex  #2 * 3 = 6

            # CHECK EVERY CELL IN THE QUADRANT!!!
            for i in range(regionSize):
                for j in range(regionSize):
                    if charToPlace == board[topLeftOfSubBoxRow + i][topLeftOfSubBoxCol + j]:      
                        return False

            return True


        def canSolveSudokuFromCell(row, col):

            # CARRY ON TO THE NEXT ROW AFTER WE VERIFY ALL COLUMNS IN PREVIOUS ROW
            if col == len(board[row]):
                col = 0
                row += 1

            # WE HAVE FINISHED THE BOARD IF WE SUCCESSFULLY GET THROUGH ALL THE BRANCHES
            if row == len(board): return True


            # Skip entries already filled out. They already have a value in them.
            if board[row][col] != EMPTY_ENTRY: return canSolveSudokuFromCell(row, col + 1)

            for value in range(1,len(board)+1):
                charToPlace = str(value)

                if canPlaceValue(row, col, charToPlace):
                    board[row][col] = charToPlace
                    # IF THE DFS OFF THIS BRANCH IS SUCCESSFUL, THEN RETURN TRUE
                    if canSolveSudokuFromCell(row, col + 1): return True

                # RESET FOR NEXT ITERATION
                board[row][col] = EMPTY_ENTRY

            return False


        EMPTY_ENTRY = '.'
        canSolveSudokuFromCell(0, 0)