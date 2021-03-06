# Create a 9x9 sudoku grid with the following rules:
# 1. Each row must contain each of the digits from 1 to 9 exactly once.
# 2. Each column must contain each of the digits from 1 to 9 exactly once.
# 3. Each of the 9 3x3 sub-grids must contain each of the digits from 1 to 9 exactly once.
# 4. The grid must be solvable.
import os

def main():
    choice = 0
    os.system('clear')
    while choice not in (1,2,3,4,5,6):
        while True: #checks if number is not in this
            try:
                print('game is loading . . .') #prints out a welcome message
                choice = int(input('\033[93m[1] Load New puzzle \n[2] Load Partially Solved Puzzle \n[3] Check solution \n[4] Solve puzzle \n[5] Save \n[6] Exit\n\033[00m')) #prints out the menu
            except UnboundLocalError:
                print('Please create or load a new board!!(1 or 2)')
            except:
                print('--------------------')
                print('\033[91m Please enter a number!\033[00m') #ANSI escape color codes
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
        os.system('clear') 
        try:
            os.system('clear')
            draw_board(board)
            print('\033[92mIf you want to go to menu, press CTRL+C, if you wanna exit the program completely, press 0 \033[00m')
            print('Please enter a number in the following format:')
            print('input will be \033[92mrow|column|digit\033[00m')
            co_ordinate = int(input('\033[92mEnter the co-ordinate \033[00m of the cell you want to change: '))#ANSI escape color codes
            co_ordinate = str(co_ordinate)
        except KeyboardInterrupt: #if user presses ctrl+C it will exit the program and go to board
            return board
        except:
            print('Please enter a number!')

        if co_ordinate == '0':
            print('\033[91mExiting . . .\033[00m')
            exit()

        elif (int(co_ordinate) >999) or (int(co_ordinate) <0):
            print('Please enter a valid co-ordinate!')
            continue #May loop back in the while loop, if not then call solve(board)
        else:
            board[int(co_ordinate[0])-1][int(co_ordinate[1])-1]=co_ordinate[2] # -1 because of a list (row,column is the format)

def draw_board(board):
    print('  123 456 789')
    print('  -----------')
    for index,row in enumerate(board):
        row = '|'.join(''.join(row[i:i+3]) for i in [0,3,6]) #Gets each 3 items in a row and puts a | in between them
        if index and index%3==0:
            print('-'*3+'+'+'-'*3+'+'+'-'*3)
        print(str(index+1)+'|'+row)
    print('  -----------')
    
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

# it works but i may add a if statemtn to decide whether to load the answer, base board or saved board
def load():
    with open('puzzleNP.txt', 'r') as f:
        board = f.read()
        board = board.split()
        board = [list(row) for row in board]
    return board

def check_solution(board):
#     board_s=[
# ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
# ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
# ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
# ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
# ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
# ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
# ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
# ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
# ['3', '4', '5', '2', '8', '6', '1', '7', '9']
# ]
#
#Board is loaded from the file instead of the array above, it creates an identical board to the one above.
    with open('puzzleNS.txt', 'r') as f:
        board_s = f.read()
        board_s = board_s.split()
        board_s = [list(row) for row in board_s]
    print(board_s)
    incorrect = 0
    for i in range(len(board_s)): #checks if the board is correct
        for j in range(len(board_s[i])):
            if board[i][j] != board_s[i][j]:
                incorrect += 1
            else:
                continue


    if incorrect == 0:
        print('Congratulations! You solved the puzzle!')
    else:
        print('Sorry, you did not solve the puzzle!, you have {} incorrect guesses'.format(incorrect))

    return board


def save(board): #probebly does not work maybe fix later???
    with open('puzzleNP.txt', 'w') as f:
        for i in range(len(board)):
            for j in range(len(board[i])):
                f.write(str(board[i][j])) #str(i)+str(j)+str(board[i][j])
            f.write('\n')
        print('Saved!')

if __name__ == "__main__":
    main()
