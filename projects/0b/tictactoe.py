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
    if winner(board) or not actions(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X: return 1
    if win == O: return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    if board == initial_state(): return 0,1

    curPlayer = player(board)
    val = float("-inf") if curPlayer == X else float("inf")

    for action in actions(board):
        curVal = getValue(result(board, action), val)

        if curPlayer == X:
            curVal = max(val, curVal)
        
        if curPlayer == O:
            curVal = min(val, curVal)
        
        if curVal != val:
            val = curVal
            ret = action
    return ret

def getValue(board, bestVal):
    if terminal(board):
        return utility(board)

    curPlayer = player(board)
    val = float("-inf") if curPlayer == X else float("inf")

    for action in actions(board):
        curVal = getValue(result(board, action), val)

        if curPlayer == X:
            if curVal > bestVal:
                return curVal
            val = max(val, curVal)
        
        if curPlayer == O:
            if curVal < bestVal:
                return curVal
            val = min(val, curVal)
    return val 