import numpy as np

N = 9
valid_inputs = [1, 2, 3,4,5,6,7,8,9]
matrix = np.zeros((N, N))

def isSafe(matrix, row, col, num):
    # Check row
    for i in range(N):
        if matrix[row][i] == num:
            return False
    
    # Check column
    for i in range(N):
        if matrix[i][col] == num:
            return False
    
    return True

def solvematrix(matrix, row, col):
    if row == N - 1 and col == N:
        return True
    
    # Move to the next row if column exceeds
    if col == N:
        row += 1
        col = 0

    # Skip filled cells
    if matrix[row][col] != 0:
        return solvematrix(matrix, row, col + 1)
    
    # Try filling the cell with each valid input
    for num in valid_inputs:
        if isSafe(matrix, row, col, num):
            matrix[row][col] = num
            if solvematrix(matrix, row, col + 1):
                return True
            matrix[row][col] = 0  # Backtrack if solution not found
    
    return False

if solvematrix(matrix, 0, 0):
    print("Solution found:")
    print(matrix)
else:
    print("No solution exists.")
