import random


def gen_random_board(n):
    board = [-1 for i in range(n)]
    for x in range(8):  # for each column
        board[x] = random.sample(range(0, n), 1)[0]
    print(board)
    return board


def get_cost(board):
    cost = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:
                cost += 1
            if abs(i-j) == abs(board[i]-board[j]):
                cost += 1
    return cost


def hill_climbing(board):
    n = len(board)
    min_cost = 100000
    i = 0
    while min_cost != 0:
        for j in range(n):
            board[i] = (board[i]+1) % n
            new_cost = get_cost(board)
            if new_cost <= min_cost:
                min_cost = new_cost
                row_val=board[i]
        board[i]=row_val
        i=(i+1)%n
    return board

# board=[0, 1, 1, 5, 2, 2, 5, 1]
#board=[7, 6, 2, 1, 6, 6, 6, 4]
# [0, 7, 7, 3, 4, 4, 5, 6]
board = gen_random_board(8)
print(get_cost(board))
print(hill_climbing(board))
