# create a Tic Tac Toe game.
# Here are the requirements:
# 2 players should be able to play the game (both sitting at the same computer)
# the board should be printed out every time a player makes a move
# you should be able to accept input of the player position and then place a symbol on the board

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
prevmove = ' '


def printboard():
    print(" " + board[6] + " | " + board[7]+ " | " + board[8] + " ")
    print(" " + board[3] + " | " + board[4]+ " | " + board[5] + " ")
    print(" " + board[0] + " | " + board[1]+ " | " + board[2] + " ")

printboard()

def acceptplayermove():
    global prevmove
    sym = raw_input('Please input your symbol')
    if sym not in ('X', 'O'):
        print('cannot make move with this sym: ' + sym)
        return
    if(sym == prevmove):
        print('sorry this is not your turn')
        return
    else:
        prevmove = sym

    pos = int(input('Please input your position'))
    if pos not in range(0, 9):
        print("Sorry, please input a number between 0-8.")
        return
    if board[pos] == ' ':
        board[pos] = sym
        checkwin(sym)
    else:
        print('cannot make this move as position non empty')
        return

def checkwin(sym):
    if (board[0] == board[1] == board[2] == sym) or (board[3] == board[4] == board[5] == sym) or (board[6] == board[7] == board[8] == sym) or (board[0] == board[3] == board[6] == sym)\
            or (board[1] == board[4] == board[7] == sym) or (board[2] == board[5] == board[8] == sym) or (board[0] == board[4] == board[8] == sym) or (board[2] == board[4] == board[6] == sym):
        print('player wins')
        return True
    else:
        return False

def countavlblpositions():
    count = 0
    for char in board:
        if char == ' ':
            count = count +1
    return count

while(countavlblpositions() > 0 and not checkwin('X') and not checkwin('O')):
    acceptplayermove()
    printboard()
