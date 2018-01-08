# create a Tic Tac Toe game.
# Here are the requirements:
# 2 players should be able to play the game (both sitting at the same computer)
# the board should be printed out every time a player makes a move
# you should be able to accept input of the player position and then place a symbol on the board

board = ['_','_','_','_','_','_','_','_','_']


def printboard():
    print(board[6], board[7], board[8])
    print(board[3], board[4], board[5])
    print(board[0], board[1], board[2])

printboard()

def acceptplayermove():
    sym = input('Please input your symbol')
    if sym not in ('X', 'O'):
        print('cannot make move with this sym: ' + sym)
        return
    pos = int(input('Please input your position'))
    if pos not in range(0, 9):
        print('cannot make move to this pos: ' + pos)
        return
    if board[pos] == '_':
        board[pos] = sym
        checkwin(sym)
    else:
         print('cannot make this move')
         return

def checkwin(sym):
    if (board[0] == board[1] == board[2] == sym):
        print('player wins')
    elif (board[3] == board[4] == board[5] == sym):
        print('player wins')
    elif (board[6] == board[7] == board[8] == sym):
        print('player wins')
    elif (board[0] == board[3] == board[6] == sym):
        print('player wins')
    elif (board[1] == board[4] == board[7] == sym):
        print('player wins')
    elif (board[2] == board[5] == board[8] == sym):
        print('player wins')
    elif (board[0] == board[4] == board[8] == sym):
        print('player wins')
    elif (board[2] == board[4] == board[6] == sym):
        print('player wins')
    else:
        print('game is still on')


acceptplayermove()
printboard()
acceptplayermove()
printboard()