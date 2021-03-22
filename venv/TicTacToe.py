import random

def display_board(board): # Function used to display the board
    print('\n' * 25)
    print(board[1] + '|' + board[2] + '|' + board[3] )
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6] )
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9] )


def player_input(): # Function to let players decide their input character for the game

    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Please choose X or O: ')
    playerOne = marker

    if playerOne == 'X':
        playerTwo = 'O'

    else:
        playerTwo = 'X'

    print(f'Player one is {playerOne}')
    print(f'Player two is {playerTwo}')

    return (playerOne,playerTwo)


def place_marker(board, marker, position): # Function used to place the player marker at selected position
    board[position] = marker
    display_board(board)
    return board


def win_check(board, mark): # Function to check if a player has won
    pass


def choose_first(): # Function to ranomdly choose which player goes first
    goFirst = random.randint(1,2)
    if goFirst == 1:
        return print('Player one goes first')
    else:
        return print('Player two goes first')


def space_check(board, position): # Function to check if a space is empty.
    if board[position] == ' ':
        return True
    else:
        return False


def full_board(board):
    pass


def player_choice(board): # Function that asks player what position they want to take
    cont = 0
    while cont == 0:
        choice = int(input("What space do you want to take (1-9): "))
        if space_check(board, choice) == True:
            return choice
            cont == 1
        else:
            print('That space is taken, choose another')


def replay(): # Function asking the player if they want to play again or exit program
    replayChoice = input('Do you want to play again?(y/n) : ')
    if replayChoice == 'y':
        print('continue')
        return True
    else:
        print('Thank you for playing!')
        return False



# print board
# player input
# place input
# check game
# repeat placing and game check till won or tie
# play again?
board = [' '] * 10
player1, player2 = player_input()
choose_first()

menu = True
while menu == True:

    display_board(board)
    positionPick = player_choice(board)
    place_marker(board, '%', positionPick)

    menu = replay()
