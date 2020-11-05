import copy

board = [['-' for i in range(3)] for i in range(3)]


def printBoard():
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(board[i][j]+' | ', end="")
            else:
                print(board[i][j], end="")
        if i != 2:
            print('\n=========')
    print('\n')


def isFree(row, column):
    if board[row][column] == '-':
        return 1
    else:
        return 0


def isGameOver(player):
    # check row:
    global ff
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != '-':
            if player == board[i][0]:
                return 1
            else:
                return -1
    # check column
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != '-':
            if player == board[0][i]:
                return 1
            else:
                return -1
    # check diagonals
    if (board[0][0] == board[1][1] == board[2][2]) and board[1][1] != '-':
        if player == board[0][0]:
            return 1
        else:
            return -1
    if (board[0][2] == board[1][1] == board[2][0]) and board[1][1] != '-':
        if player == board[0][2]:
            return 1
        else:
            return -1
    # checks if there is still a possible move
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                # print( 'Game not over')
                return 100
    # tie
    return 0


def possibleMoves():  # returns a list of all possible free spaces
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                moves.append([i, j])
    return moves


def MaxValue(a, b):
    result = isGameOver('X')
    if result != 100:
        return result,None
    bestVal = -1000
    bestAction=None
    for move in possibleMoves():
        board[move[0]][move[1]] = 'X'
        val ,_= MinValue(a, b)
        if bestVal<val:
            bestVal=val  
            bestAction=move         
        bestVal = max(bestVal, val)
        board[move[0]][move[1]] = '-'
        if bestVal >= b:
            return bestVal,bestAction
        a = max(a, bestVal)
    return bestVal,bestAction

def MinValue(a, b):
    result = isGameOver('X')
    if result != 100:
        return result,None
    bestVal = 1000
    bestAction=None
    for move in possibleMoves():
        board[move[0]][move[1]] = 'O'
        val,_ = MaxValue(a, b)
        if bestVal>val:
            bestVal=val  
            bestAction=move         
        bestVal = min(bestVal, val)
        board[move[0]][move[1]] = '-'
        if bestVal <= a:
            return bestVal, bestAction
        b = min(b, bestVal)
    return bestVal, bestAction


def AlphaBeta():
    v,action = MaxValue(-1000, 1000)
    board[action[0]][action[1]]='X'
    return board


def getUserInput():
    r = int(input("Enter row(0,1,2): "))
    c = int(input("Enter column(0,1,2): "))
    if(isFree(r, c)):
        board[r][c] = 'O'
        return 1
    else:
        print('\nPosition not free!\n')
    return 0


print('Computer is X, Player is O\n')

while(isGameOver('X') == 100 and isGameOver('O') == 100):
    print("Player X\'s Turn")
    board = AlphaBeta()
    printBoard()
    if (isGameOver('X') == 100 and isGameOver('O') == 100):
        while True:
            x = getUserInput()
            if x == 1:
                break
        print("Player O's Turn:")
        printBoard()
    else:
        break


print('GAME OVER\n++++++++++++')
result = isGameOver('X')
if result == 1:
    print('COMPUTER WON!')
elif result == -1:
    print('YOU WON!')
else:
    print('TIE!')

"""
OUTPUT

Computer is X, Player is O

Player X's Turn
X | - | -
=========
- | - | -
=========
- | - | -

Enter row(0,1,2): 0
Enter column(0,1,2): 2
Player O's Turn:
X | - | O
=========
- | - | -
=========
- | - | -

Player X's Turn
X | - | O
=========
X | - | -
=========
- | - | -

Enter row(0,1,2): 2
Enter column(0,1,2): 0
Player O's Turn:
X | - | O
=========
X | - | -
=========
O | - | -

Player X's Turn
X | - | O
=========
X | X | -
=========
O | - | -

Enter row(0,1,2): 1
Enter column(0,1,2): 2
Player O's Turn:
X | - | O
=========
X | X | O
=========
O | - | -

Player X's Turn
X | - | O
=========
X | X | O
=========
O | - | X

GAME OVER
++++++++++++
COMPUTER WON!
"""
