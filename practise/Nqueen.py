
import numpy as np
global N
N = 4

def issafe(matrix, row, col):
      # Assuming N is the size of the square matrix
    # Check column
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if matrix[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if matrix[i][j] == 1:
            return False
    
    for i in range(col):
            if matrix[row][i] == 1:
                return False
    return True

def SolveNqueen(matrix,column_to_solve):
    if column_to_solve >=N:
        return True
    for i in range(N):
        if issafe(matrix,i,column_to_solve):
            matrix[i][column_to_solve] = 1
            if  SolveNqueen(matrix,column_to_solve+1)==True:
                return True
            matrix[i][column_to_solve] = 0
    return False

matrix  = np.zeros((N,N),dtype=int)
SolveNqueen(matrix,0)
print(matrix)
            