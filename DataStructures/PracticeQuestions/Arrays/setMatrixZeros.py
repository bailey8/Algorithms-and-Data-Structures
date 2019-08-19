class Solution(object):

    def setZeroes(self, matrix):
        def zero(matrix,rowIndex,columnIndex):
            # Clear column
            for row in range(len(matrix)):
                matrix[row][columnIndex] = 0
            # Clear row
            for col in range(len(matrix[0])):
                matrix[rowIndex][col] = 0
        
        #Stores coords of all zeros
        answer = []
        # Record coords of all 0s
        for row,arr in enumerate(matrix):
            for col,element in enumerate(arr):
                if element == 0: answer.append((row,col))
        # zero out each coord
        for row,col in answer:
            zero(matrix,row,col)
            