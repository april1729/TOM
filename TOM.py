from Board import Board
from Move import Move
import numpy
import math


inf = 100000000000000000000000000


def TOM(depth):
    b = Board(1)
    turn=0
    while not b.isGameOver:
        turn=turn+1

        if b.whoseTurn == 1:
            move = getMinimaxMove(b, depth)
            b.makeMove(move)
            print("your value:"+str(b.rateBoardOverall(2)))
            print("my value: "+str(b.rateBoardOverall(1)))
            print("turn "+str(turn))
            b.printBoard()
        else:
            move = promptMove(b)
            #move = getMinimaxMove(b, depth)

            b.makeMove(move)
    return 0


def getMinimaxMove(board, depth):
    if board.whoseTurn == 1:
        bestVal = -1*inf
    else:
        bestVal = inf

    bestMove = None
    for move in board.getAllMoves():
        if board.whoseTurn==1:
            moveVal=minimax(move, board, depth, True, -inf, inf)
           # print("entry: "+str(move.entry)+" value: "+str(moveVal))

            if moveVal > bestVal:
                bestMove = move
                bestVal = moveVal

        else:
            moveVal=minimax(move, board, depth, False, -inf, inf)
            #print("entry: "+str(move.entry)+" value: "+str(moveVal))

            if moveVal < bestVal:
                bestMove=move
                bestVal=moveVal
    if math.fabs(bestVal)>1000:
        print("gg")

    return bestMove


def promptMove(board):
    if board.mainBoardMatrix[board.lastBoard%3, math.floor(board.lastBoard/3)]==0:
        subboard=board.lastBoard;
        print("Your move is in board"+str(board.lastBoard))
    else:
        subboard=input("What board?")
    entry = input("what square? ")

    return Move(2, int(subboard), int(entry))


def minimax(node, board, depth, maximizingPlayer, alpha, beta):
    newBoard = board.__copy__()
    newBoard.makeMove(node)
    if depth == 0 or newBoard.isGameOver:
        bestValue = newBoard.rateBoardOverall(1) - newBoard.rateBoardOverall(2)
        return bestValue
    if maximizingPlayer:
        bestValue = -1*inf
        for child in newBoard.getAllMoves():
            val = minimax(child, newBoard, depth - 1, False, alpha, beta);
            bestValue = max(bestValue, val)
            alpha=max(alpha, bestValue)
            if alpha>=beta:
                break
        return bestValue
    else:
        bestValue = inf
        for child in newBoard.getAllMoves():
            val = minimax(child, newBoard, depth - 1, True, alpha, beta)
            bestValue = min(bestValue, val)
            beta=min(beta, bestValue)
            if alpha>=beta:
                break


        return bestValue


if __name__ == '__main__':
    TOM(4)
