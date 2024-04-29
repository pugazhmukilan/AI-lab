import random

def print_board(matrix):
     for row in matrix :
         print(" | ".join(row))
         print("\n")
def checkboard(matrix,symbol):
    
    for row in matrix:
        if all (cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(matrix[row][col] == symbol for row in range(3)):
            return True
    diagonal1 = all(matrix[i][i] == symbol for i in range(3))
    diagonal2 = all(matrix[i][2 - i] == symbol for i in range(3))
    if diagonal1 or diagonal2:
        return True
    return False

def is_board_full(matrix):
    for row in matrix:
        for j in row:
            if j == " ":
                return False
    return True

def user_move(matrix):
    while True:
        try:
            row = int(input("Enter the row (1, 2, or 3): ")) - 1
            col = int(input("Enter the column (1, 2, or 3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and matrix[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Please enter a valid row and column.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer_move(matrix):
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if matrix[row][col] == " ":
            return row,col
 
def play_game():
    matrix = [[" " for _ in range(3)] for _ in range (3)]   
    print("welcome to tic tac tao game")
    
    
    while True:
        user_row,user_col = user_move(matrix)
        matrix[user_row][user_col] = "X"
        print_board(matrix)
        
        if checkboard(matrix ,"X"):
            print("Congrulations you have wont the game")
            break
        
        if is_board_full(matrix):
            break
        
        computer_row,computer_col = computer_move(matrix)
        matrix[computer_row][computer_col] = "O"
        if (checkboard(matrix,"O")):
            print("OOPS!! computer ahve won the game")
            break
        print_board(matrix)
        
        
        if is_board_full(matrix):
            break
        
        
play_game()     
            