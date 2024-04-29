import numpy as np

N = 3
valid_inputs = [1, 2, 3,]
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

def solvematrix(matrix, row, col, solutions):
    if row == N - 1 and col == N:
        print(matrix)
        
        solutions.append(np.copy(matrix))#appending the solution in the list
        return True
    
    # Move to the next row if column exceeds
    if col == N:
        row += 1
        col = 0

    # Skip filled cells
    if matrix[row][col] != 0:
        return solvematrix(matrix, row, col + 1, solutions)
    
    # Try filling the cell with each valid input
    for num in valid_inputs:
        if isSafe(matrix, row, col, num):
            matrix[row][col] = num
            solvematrix(matrix, row, col + 1, solutions)
            matrix[row][col] = 0  # Backtrack
    
    return False

solutions = []
solvematrix(matrix, 0, 0, solutions)

if solutions:
    print("Total solutions found:", len(solutions))
    for idx, sol in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        print(sol)
else:
    print("No solution exists.")
