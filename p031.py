#!/usr/bin/python
import euler

UKCoins = [200, 100, 50, 20, 10, 5, 2, 1]
USCoins = [25, 10, 5, 1]

def make_board(c):
    board = []
    for x in range(len(c)+1):
        board.append({})
    return board

def numways(amount, c, board):
    assert amount >= 0
    if not c:
        return 0
    if amount == 0:
        return 1
    if amount < c[0]:
        return numways(amount, c[1:], board, t)

    if not amount in board[len(c)]:
        if (len(c) == 1):
            board[len(c)][amount] = 1
        else:
            maxC = amount // c[0]
            board[len(c)][amount] = sum(map(lambda n: numways(amount - n*c[0], c[1:], board), range(maxC+1)))
    
    return board[len(c)][amount]

print(numways(200, UKCoins, make_board(UKCoins)))
