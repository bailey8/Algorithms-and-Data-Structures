class Solution:
    def rotate(self, matrix):
        
        n = len(matrix)
        
        # TRANSPOSE THE MATRIX
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
                
        # REVERSE EACH ROW
        for i in range(n):
            matrix[i].reverse()
