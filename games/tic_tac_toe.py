# LIBRARIES IMPORT

from IPython.display import clear_output

# DEPENDENCIES

def display_board(board):
    clear_output()
    print(' ', board[7], ' | ', board[8], ' | ', board[9])
    print('-----------------')
    print(' ', board[4], ' | ', board[5], ' | ', board[6])
    print('-----------------')
    print(' ', board[1], ' | ', board[2], ' | ', board[3])

def player_input():
    player1 = input("Player 1: please pick a marker between 'X' and 'O': ")
    while player1 != 'X' and player1 != 'O':
        player1 = input("Wrong pick! Please choose between 'X' and 'O': ")
    print('Player 1 chose marker: ', player1)
    return player1

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    win = False
    # first row wins
    if board[7]==mark and board[8]==mark and board[9]==mark:
        win = True
    # second row wins
    if board[4]==mark and board[5]==mark and board[6]==mark:
        win = True
    # third row wins
    if board[1]==mark and board[2]==mark and board[3]== mark:
        win = True
    # first column wins
    if board[7]==mark and board[4]==mark and board[1]==mark:
        win = True
    # second column wins
    if board[8]==mark and board[5]==mark and board[2]==mark:
        win = True
    # third column wins
    if board[9]==mark and board[6]==mark and board[3]== mark:
        win = True
    # first diagonal wins
    if board[7]==mark and board[5]==mark and board[3]== mark:
        win = True
    # second diagonal wins
    if board[1]==mark and board[5]==mark and board[9]== mark:
        win = True

    return win

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    return ' ' not in board

def player_choice(board):
    choice = input("Please, select next position (choose using your number pad -> number between 1 and 9): ")
    choice = int(choice)
    print('You chose position: ', choice)
    return choice

def replay():
    question = input('Do you want to play again? (Type Y for Yes or N for No): ')
    while question != 'Y' and question != 'N':
        question = input("Wrong pick! Please choose between 'Y' and 'N': ")
    return question == 'Y'


# GAME

play_more = True

while play_more == True:

    print('Welcome to Tic Tac Toe!')

    # Select Player 1 marker
    player1 = player_input()
    print(player1)
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    # Display empty board
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # Init win variable to False (so game can loop)
    win = False

    # Init turn number
    turn = 1

    while win==False or full_board_check(board)==False:

        # Player 1 Turn (odd turns)
        if turn%2 != 0:
            # Ask player to choose position and checks if position is available
            choice = player_choice(board)
            while space_check(board, choice)==True and full_board_check(board)==False:
                # Place maker on board
                place_marker(board,player1,choice)
                # Display new board
                display_board(board)

            # Check if this is a win
            win = win_check(board,player1)
            if win:
                print('Congratulations! Player 1 wins the game!')
                play_more = replay()
                if not play_more:
                    print('The game has ended. Thank you for playing!')
                    break
                else:
                    break
            if full_board_check(board)==True:
                print('Board full...The game has ended.')
                play_more = replay()
                if not play_more:
                    print('The game has ended. Thank you for playing!')
                    break
                else:
                    break
            turn += 1

        # Player 2 Turn (even turns)
        if turn%2 == 0:
            # Ask player to choose position and checks if position is available
            choice = player_choice(board)
            while space_check(board, choice)==True and full_board_check(board)==False:
                # Place maker on board
                place_marker(board,player2,choice)
                # Display new board
                display_board(board)

            # Check if this is a win
            win = win_check(board,player2)

            if win:
                print('Congratulations! Player 2 wins the game!')
                play_more = replay()
                if not play_more:
                    print('The game has ended. Thank you for playing!')
                    break
                else:
                    break
            if full_board_check(board)==True:
                print('Board full...The game has ended.')
                play_more = replay()
                if not play_more:
                    print('The game has ended. Thank you for playing!')
                    break
                else:
                    break
            turn += 1
