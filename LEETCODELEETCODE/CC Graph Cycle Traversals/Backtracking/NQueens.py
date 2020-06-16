class Solution:
    def solveNQueens(self,numberOfQueens):
        
        # Check if a column placement that we just put in the queenPlacementPerRow list is actually valid to recurse on
        def isValid(queenPlacementPerRow, rowWeAreValidatingOn):

            # rowWeAreValidatingOn is the row that we just placed a queen on and we need to validate the placement
            #rowWeAreValidatingOn = len(queenPlacementPerRow) - 1
    
            # Loop and check our placements in every row previous against the placement that we just made
            for row in range(rowWeAreValidatingOn):
                """
                Get the absolute difference between:
                1.) The column of the already placed queen we are comparing against -> queenPlacementPerRow.get(ithQueenRow)
                2.) The column of the queen we just placed -> queenPlacementPerRow.get(rowWeAreValidatingOn)
                """
                absoluteColumnDistance = abs(queenPlacementPerRow[row] - queenPlacementPerRow[rowWeAreValidatingOn])

                """
                1.) absoluteColumnDistance == 0
                    If the absolute difference in columns is 0 then we placed in a column being
                    attacked by the i'th queen.
                2.) absoluteColumnDistance == rowDistance
                    If the absolute difference in columns equals the distance in rows from the
                    i'th queen we placed, then the queen we just placed is attacked diagonally. # DIAGONAL ISSUE
                For Constraint #2 imagine this:
                [
                    ". . Q .",  <--- row 0 (Queen 1)
                    "Q . . .",  <--- row 1 (Queen 2)
                    ". Q . .",  <--- row 2 (Queen 3)
                    ". . . ."
                ]
                1.) 
                    Absolute Column Distance Between Queen 2 & 3 == 1.
                    Queen 2 is in col 0, Queen 3 is in col 1. 1 - 0 = 1.
                2.)
                    Absolute Row Distance Between Queen 2 & 3 == 1
                    Queen 2 is in row 1, Queen 3 is in row 2. 2 - 1 = 1.
                """
                rowDistance = rowWeAreValidatingOn - row
                if absoluteColumnDistance == 0 or absoluteColumnDistance == rowDistance: return False
            
            return True

        """
        [
        ".Q..",
        "...Q",
        "Q...",
        "..Q."
        ]
        Generate a board from the list of column placements for each of the n rows.
        """
        def generateBoardFromPlacements(queenPlacementPerRow):

            board = []
            numberOfRows = len(queenPlacementPerRow)

            
            # Materialize a row for each queen that we placed
            for row in range(numberOfRows):

            # Go through all columns in the row and populate the string.
            # If the column has a queen in it place a 'Q', otherwise place a '.'
                newRow = []
                for col in range(numberOfQueens):
                    # IF A QUEEN IS IN THIS COLUMN FOR THIS ROW, THEN RECORD SO
                    if col == queenPlacementPerRow[row]: newRow.append('Q')
                    else: newRow.append('.')
                board.append("".join(newRow))

            return board
     

        def solveNQueensHelp(row):

            # All n queens have been placed in the n rows. We have reached the bottom of our recursion. 
            # We can now add the queenPlacementPerRow to the results.
            if row == numberOfQueens: 
                results.append(generateBoardFromPlacements(queenPlacementPerRow))
                return

            """
                Try all columns in the current row that we are making
                a choice on.
                The queenPlacementPerRow list will hold the column we place a
                queen for the i'th row.
                So if I have [ 1, 3, 0, 2 ] that means:
                It is a 4 x 4 board.
                row index 0 has a queen placed in column index 1
                row index 1 has a queen placed in column index 3
                row index 2 has a queen placed in column index 0
                row index 3 has a queen placed in column index 2
            """
            # TRY TO PLACE THE QUEEN IN EVERY COLUMN
            for col in range(numberOfQueens):

                # PLACE THE QUEEN IN THE DESIRED COLUMN
                queenPlacementPerRow[row] = col

                # If it is a valid placement we recurse to work on the next row (row + 1) in a recursive call
                if isValid(queenPlacementPerRow,row): solveNQueensHelp(row + 1)
    
        
        results = []
        queenPlacementPerRow = [0]*numberOfQueens
        solveNQueensHelp(0)
        return results

            


def hi():
    word = "h"
    if word: print("tes")

hi()