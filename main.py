# Create a 9x9 sudoku grid with the following rules:
# 1. Each row must contain each of the digits from 1 to 9 exactly once.
# 2. Each column must contain each of the digits from 1 to 9 exactly once.
# 3. Each of the 9 3x3 sub-grids must contain each of the digits from 1 to 9 exactly once.
# 4. The grid must be solvable.
import os

def main():
    choice = 0
    while choice not in (1,2,3,4,5,6):
        print('aaa')
        while True: #checks if number is not in this
            try:
                print('game is starting . . .') #prints out a welcome message
                choice = int(input('[1] Load New puzzle \n[2] Load Partically Solved Puzzle \n[3] Check solution \n[4] Solve puzzle \n[5] Save \n[6]Exit\n')) #prints out the menu
            except:
                print('--------------------')
                print('Please enter a number!')
                print('--------------------')
            else:
                if choice == 1:
                    print('New puzzle is loading . . .')
                    board = new_board()
                    draw_board(board)
                elif choice == 2:
                    print('saved file is loading . . .')
                    board = load()
                    draw_board(board)
                elif choice == 3:
                    print('Checking your answers . . .')
                    check_solution(board)
                elif choice == 4:
                    print('entering puzzle solving mode . . .')
                    board = solve(board)
                elif choice == 5:
                    print('Saving puzzle . . .')
                    save(board)
                elif choice == 6:
                    print('Exiting . . .')
                    exit()
                else:
                    print('Please enter a valid number')

def solve(board):
    looping = True
    while looping:
        try:
            print('If you want to exit, just press enter')
            co_ordinate = int(input('Enter the co-ordinate of the cell you want to change: '))
            co_ordinate = str(co_ordinate)
            os.system('cls') #not tested yet, check if its correct
        except:
            print('Please enter a number!')
        
        if co_ordinate == '':
            return board

        if co_ordinate == '0':
            exit()
            
        
        elif (int(co_ordinate) >999) or (int(co_ordinate) <0):
            print('Please enter a valid co-ordinate!')
            continue #May loop back in the while loop, if not then call solve(board)
        else:
            board[int(co_ordinate[0])-1][int(co_ordinate[1])-1]=co_ordinate[2] # -1 because of a list (row,column is the format)
            draw_board(board)





def draw_board(board):
    for index,row in enumerate(board):
        row = '|'.join(''.join(row[i:i+3]) for i in [0,3,6]) #Gets each 3 items in a row and puts a | in between them
        if index and index%3==0:
            print('-'*3+'+'+'-'*3+'+'+'-'*3)
        print(row)

def new_board():
    board= [
['5','3','0','0','7','0','0','0','0'],
['6','0','0','1','9','5','0','0','0'],
['0','9','8','0','0','0','0','6','0'],
['8','0','0','0','6','0','0','0','3'],
['4','0','0','8','0','3','0','0','1'],
['7','0','0','0','2','0','0','0','6'],
['0','6','0','0','0','0','2','8','0'],
['0','0','0','4','1','9','0','0','5'],
['0','0','0','0','8','0','0','7','9']
]
    return board


def load():
    pass


def check_solution(board):
    board_s=[
['5', '3', '4', '6', '7', '8', '9', '1', '2'],
['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
['3', '4', '5', '2', '8', '6', '1', '7', '9']
]
    #board_s = [list(map(int, row)) for row in board_s]
    #Change this forloop later to include a enumerate function
    incorrect = 0
    for i in range(len(board_s)): #checks if the board is correct
        for j in range(len(board_s[i])):
            if board[i][j] != board_s[i][j]:
                incorrect += 1
    if incorrect == 0:
        print('Congratulations! You solved the puzzle!')
    else:
        print('Sorry, you did not solve the puzzle!, you have {} incorrect guesses'.format(incorrect))

    return board
                
                

def save(board):
    pass


if __name__ == "__main__":
    main()