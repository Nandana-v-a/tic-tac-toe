def display(board):
    print('\n')
    print('  '+board[7]+' | '+board[8]+' | '+board[9]+'  ')
    print('----|---|----')
    print('  '+board[4]+' | '+board[5]+' | '+board[6]+'  ')
    print('----|---|----')
    print('  '+board[1]+' | '+board[2]+' | '+board[3]+'  ')
    print('\n')


def user_input(turn):
    choice='Wrong'
    while choice.isdigit()==False or int(choice) not in range(1,10):
        choice=input(f'{turn},Please enter the number in 1-9:')
        if not choice.isdigit():
            print('sorry! you are not entered digit')
        elif choice.isdigit() and int(choice) not in range(1,10):
            print('sorry! you entered out of range')
            choice='wrong'
    return int(choice)

def player_input(turn,players):
    player1 = ' '
    player2 = ' '
    while not (player1 == 'X' or player1 == 'O' or player2 == 'X' or player2 == 'O'):
        if turn == players[1]:
            player1=input('please choose your symbol among X and O :').upper()
        else:
            player2=input('please choose your symbol among X and O :').upper()
    if player1 =='X':
        player2 = 'O'
    elif player1 == 'O' :
        player2 = 'X'
    elif player2 == 'X':
        player1 = 'O'
    else:
        player1 = 'X'
    return (player1,player2)

def board_maker(board,maker,position):
    board[position]=maker

def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) or
            (board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[1]==mark and board[4]==mark and board[7]==mark) or
            (board[1]==mark and board[5]==mark and board[9]==mark) or
            (board[3]==mark and board[5]==mark and board[7]==mark) or
            (board[3]==mark and board[6]==mark and board[9]==mark) or
            (board[2]==mark and board[5]==mark and board[8]==mark))


def space_check(board,position):
    return board[position] == ' '

def fullboard_check(board):
    for i in range(1,10):   
        if space_check(board,i):
            return False
    return True

def replay():
    return input("Are you ready to play game again enter Yes or No : ").lower().startswith('y')

import random
def choose_first(players):
    if random.randint(0,1) == 0:
        return players[1]
    else :
        return players[2]



def player_choice(board,turn):
    position = user_input(turn)
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('choose your next position: (1-9) '))
    return position


def players_name():
    players = ['0','','']
    while ('' in players) or (len(set(players))!=3):
        print('(Note: Name should be unique and not be empty)')
        players[1] = input('Player1: please enter your name :')
        players[2] = input('Player2: please enter your name :')
    return players

#from here the game code start

print("welcome to the tic tac toe Game")
while True:
    print("If you want to quit anytime enter Q or q")
    #Reset the board
    board = [' ']*10
    players = players_name()
    turn = choose_first(players)
    print(f'{turn} will go first')
    player1_mark,player2_mark=player_input(turn,players)
    play_game = input('Are you ready to enter the game enter Yes or No :')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == players[1]:
            #player1 turn
            display(board)
            position = player_choice(board,turn)
            board_maker(board,player1_mark,position)
            
            if win_check(board,player1_mark):
                display(board)
                print(f'Congradulations! {turn} have won the game!')
                game_on=False
            else:
                if fullboard_check(board):
                    display(board)
                    print('the game is draw!')
                    break
                else:
                    turn = players[2]
        else:
            #player2 turn
            display(board)
            position = player_choice(board,turn)
            board_maker(board,player2_mark,position)
            
            if win_check(board,player2_mark):
                display(board)
                print(f'Congradulations! {turn} have won the game!')
                game_on=False
            else:
                if fullboard_check(board):
                    display(board)
                    print('the game is draw!')
                    break
                else:
                    turn = players[1]
    if not replay():
        break