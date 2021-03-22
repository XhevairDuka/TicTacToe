# coding along with milestone project 1 pierian video
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
        marker = input('Please choose X or O: ').upper() # added .upper so if user enters x or o will auto upper
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
#added checks for win
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal




def choose_first(): # Function to randomly choose which player goes first
    goFirst = random.randint(1,2)
    if goFirst == 1:
        print('Player one goes first')
        return 'Player 1'
    else:
        print('Player two goes first')
        return 'Player 2'


def space_check(board, position): # Function to check if a space is empty.
    return board[position] == ' ' # condensed if-else to just return



def full_board(board): # Function to check if board is full
    for i in range(1,10): # for loop to iterate through board
        if space_check(board, i): # use space_check function to check if place is empty, returns False
            return False
    return True # if for loops exits return True, board is full



def player_choice(board): # Function that asks player what position they want to take
    position= 0 # improved function
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("What space do you want to take (1-9): "))

    return position




def replay(): # Function asking the player if they want to play again or exit program
    replayChoice = input('Do you want to play again?(y/n) : ')
    return replayChoice == 'y'




# print board
# player input
# place input
# check game
# repeat placing and game check till won or tie
# play again?
print('Welcome to TicTacToe')
while True:

    board = [' '] * 10
    player1, player2 = player_input()
    turn = choose_first()

    play_game = input('Ready to play? (y/n) :')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False


    while game_on:

        if turn == 'Player 1':
            # Show board
            display_board(board)
            # Choose position
            positionPick = player_choice(board)
            # Place marker @ position
            place_marker(board, player1, positionPick)
            # Check for win
            if win_check(board,player1):
                display_board(board)
                print('Player 1 has won!')
                game_on = False
            # Check for tie
            else:
                if full_board(board):
                    display_board(board)
                    print('Game is tied')
                    game_on = False
                else:
                    turn = 'Player 2'
            # Next players turn
        else:
            # Show board
            display_board(board)
            # Choose position
            positionPick = player_choice(board)
            # Place marker @ position
            place_marker(board, player2, positionPick)
            # Check for win
            if win_check(board,player2):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            # Check for tie
            else:
                if full_board(board):
                    display_board(board)
                    print('Game is tied')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
