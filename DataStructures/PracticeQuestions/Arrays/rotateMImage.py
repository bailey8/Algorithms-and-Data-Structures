def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range (0,rows):
        for col in range(row,cols):
            matrix[row][col],matrix[col][row] = matrix[col][row], matrix[row][col]
    for row in matrix:
        row.reverse()
 