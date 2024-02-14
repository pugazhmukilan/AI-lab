import numpy as np
import sys
global N
N=10




def issafe(matrix,row,col):
    
    # for the left diagonal
    for i,j in zip(range(row, -1,-1), range(col, -1,-1)): 
        
        if matrix[i][j]==1:
            
            return False
        
    #for the rright diagonal
    for  i, j in zip(range(row, N ,1) ,range(col, N ,1)): 
        if matrix[i][j]==1 :
            return False
    #checking in the particular row   
    for i in range(col):
        if matrix[row][i]==1:
            return False
    return True   
        
def solveNqueen(matrix,column_to_solve):
    if column_to_solve>=N:
        return True
    
    for i in range(N):
        if issafe(matrix,i,column_to_solve):
            
            matrix[i][column_to_solve]=1
            
            if solveNqueen(matrix,column_to_solve+1)==True:
                print("wait for some time")
                
                return True
            
            
            matrix[i][column_to_solve]=0
            
    return False
            
def printmatrix(matrix):
    for  i in range(N):
        print("\n")
        for j in range(N):
            if matrix[i][j]==1:
                print(" Q ",end=" ")
            else:
                print(" . ",end=" ")
    
    
def start():
    print("started")
    for i in range(N):
        matrix=np.zeros((N,N))
        print("possiblity ",i,)
        if solveNqueen(matrix,i):
            printmatrix(matrix)
            return True
            
        print("\n\n\n\n")
        
        
    print(matrix)
    
start()