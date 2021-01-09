"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    totalX = 0
    totalO = 0
    totalE = 0
    for b in board:
        for element in b:
            if element == X: totalX+=1
            if element == O: totalO+=1
            if element == EMPTY: totalE+=1
    # empty board
    if totalE == 9:
        return X
    if totalX > totalO:
        return O
    if totalX == totalO:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == EMPTY:
                possibleActions.append((r,c))
    return possibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    currentPlayer = player(board)
    modifiedBoard = deepcopy(board)
    # modify board
    modifiedBoard[action[0]][action[1]] = currentPlayer
    return modifiedBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winningRun = len(board)
    winningCombos = [
                     [(0, 0), (0, 1), (0, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(0, 2), (1, 1), (2, 0)]
                    ]
    for combo in winningCombos:
        xCount = 0
        oCount = 0
        for i, j in combo:
            if board[i][j] == X:
                xCount+=1
            if board[i][j] == O:
                oCount+=1
        if xCount == winningRun:
            return X
        if oCount == winningRun: 
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
