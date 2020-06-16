class Solution(object):
    def setZeroes(self, matrix):

        # RECORD WHICH ROWS HAVE A ZERO AND WHICH COLUMNS
        rowsToBeDeleted, colsToBeDeleted =  set(), set()

        # FOR EACH ROW IN THE COLUNN
        for row in range(len(matrix)):

            # FOR EACH COLUMN IN THE ROW
            for col in range(len(matrix[0])):
                # IF THE CELL IS 0, ADD BOTH IT'S ROW AND COL TO SETS TO BE DELETED LATER
                if matrix[row][col] == 0: 
                    rowsToBeDeleted.add(row)
                    colsToBeDeleted.add(col)

        # ZERO OUT ALL THE ROWS AND COLUMNS WE MARKED FOR DELETION
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in rowsToBeDeleted or col in colsToBeDeleted:
                    matrix[row][col] = 0
                





class Solution2(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # IF AN ELEMENT IN THE FIRST ROW IS 0, THEN MATRIX[0][0] WILL BE SET TO 0
        # THIS WILL TRIGGER THE FLAG FOR THE 1ST COLUMN, WHICH WE DONT WANT UNLESS MATRIX[0][0] 
        # IS ACTUALLY 0 (BEFORE THE FLAG IS SET). TO STILL USE MATRIX[0][0] AS A FLAG, WE HAVE TO SAVE THE STATE
        # OF THE CELL BEFORE WE ZERO IT
        flag = False
        
        for row in range(len(matrix)):
            
            # WE CANT USE MATRIX[0][0] AS A COLUMN FLAG, BC IT IS THE FLAG FOR THE FIRST ROW,
            # SO INSTEAD USE THIS FLAG VARIABLE FOR THE FIRST ROW
            if matrix[row][0] == 0:
                flag = True
                
            # WE DONT WANT TO CHECK THE FIRST COLUMN BC IF IT IS ZERO THEN WE WILL TRIGGER THE MATRIX[0][0] FLAG,
            #WHICH SHOULD ONLY BE TRIGGERED BY ELEMENTS IN THE FIRST ROW
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
            
        
        # WE NEED TO DO THIS STEP FIRST, BEFORE ZEROING THE FIRST ROW OR FIRST COLUMN
        # BC IF WE ZERO THOSE FIRST THEN OUR FLAGS WILL BE USELESS (THEY WILL ALL BE ZERO!!!
        # SKIP THE FIRST ROW AND FIRST COLUMN, BC WE DONT WANT TO MODIFY OUR FLAGS UNTIL WE ARE FINISHED USING THEM
        # WE DONT WANT TO MODIFY OUR FLAGS BEFORE WE ARE FINISHED!!
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
                    
        if matrix[0][0] == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
        if flag:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        
                    
        