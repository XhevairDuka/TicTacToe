# My simple example of a TIC TAC TOE game
# There is no win check. That would be done by the players as they play.

def display(row1, row2, row3):  # function to display the current game board
    print("***GAME BOARD***")
    print(row1)
    print(row2)
    print(row3)


def continue_game(game_on):  # function asks the player if they want to continue the game.
    choice = 'nothing'  # placeholder for the choice variable
    while choice not in ['y', 'n']:
        choice = input('Do you want to keep playing? (y,n): ')

        if choice not in ['y', 'n']:   # if the user types anything in except y or n
            print('Please choose only y or n')
        if choice == 'y':  # returns true to continue the game
            return True
        else:  # returns false to end game
            print("Thank you for playing!")
            return False


def game():  # main function for the game
    game_on = True
    while game_on:
        display(row1, row2, row3)

        rowchoice = int(input("Choose a row(1-3): "))

        columnchoice = int(input(f"Choose a column in row {rowchoice}(1-3): ")) - 1

        if rowchoice == 1:
            if row1[columnchoice] is ' ':
                row1[columnchoice] = input("Type in the character you want: ")
            else:
                print('This space is taken, try again')
                pass
        elif rowchoice == 2:
            if row2[columnchoice] is ' ':
                row2[columnchoice] = input("Type in the character you want: ")
            else:
                print('This space is taken, try again')
                pass
        elif rowchoice == 3:
            if row3[columnchoice] is ' ':
                row3[columnchoice] = input("Type in the character you want: ")
            else:
                print('This space is taken, try again')
                pass
        else:
            print("Try again")

        display(row1, row2, row3)
        game_on = continue_game(game_on)



row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

print("TIC TAC TOE")
print("Player One is X")
print("Player Two is O")

game()

