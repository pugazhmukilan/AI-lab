import numpy as np

N = 4
valid_inputs = [1,2,3,4]
def is_safe(matrix,row,col,num):
    for i in range(N):
        if matrix[i][col] == num :
            return False
    for i in range(N):
        if matrix[row][i] == num :
            return False
    return True

def solvematrix(matrix,row,col,solutions):
    if row == N-1 and col ==N:
        solutions.append(np.copy(matrix))
        return True
    #if column ends but row doesnt in the matrix
    if col == N:
        col = 0
        row +=1
    
    #if box is filled with number recussiion with column +1
    if matrix[row][col] !=0:
        solvematrix(matrix,row,col+1,solutions)
    
    #itterating throught the vaild inputs and checking the correct number to be placed
    for num in valid_inputs:
        if is_safe(matrix,row,col,num):
            matrix[row][col]=num
            solvematrix(matrix,row,col+1,solutions)
            matrix[row][col] = 0   # Res
            
    return False

matrix = np.zeros((N,N))
solutions = []
solvematrix(matrix,0,0,solutions)

for i in range(len(solutions)):
    print(f"Solution {i+1}:")
    print(solutions[i])
    print("\n")
        
        