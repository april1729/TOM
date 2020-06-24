import math
import numpy
from Move import Move
import random


class Board:
    def __init__(self, whoseTurn):
        self.boardMatrix = numpy.zeros((9, 9))
        self.mainBoardMatrix = numpy.zeros((3, 3))
        self.isGameOver = False
        self.lastBoard = 5
        self.whoseTurn = whoseTurn

    def makeMove(self, move):
        player = move.player
        subBoard = move.board
        entry = move.entry

        r = subBoard % 3
        c = math.floor(subBoard / 3)

        re = entry % 3
        ce = math.floor(entry/3)

        self.boardMatrix[3*r+re, 3*c+ce]=player

        if self.isWon(self.getSubBoard(subBoard)):
            self.mainBoardMatrix[r, c] = player
            if self.isWon(self.mainBoardMatrix):
                self.isGameOver = True

        self.lastBoard = entry

        if player == 1:
            self.whoseTurn = 2
        else:
            self.whoseTurn = 1

    def getSubBoard(self, n):
        # n is number 1-9
        r = n % 3
        c = math.floor(n / 3)

        startRow=3*r;
        startCol=3*c;
        return self.boardMatrix[startRow:startRow+3,startCol:startCol+3]

    def rateBoardOverall(self,player):

        if self.whoIsWinner()==player:
            return 10000
        else:
            sum=0
            for i in range(0,9):
                r=i%3
                c=math.floor(i/3)
                if self.mainBoardMatrix[r,c]==0:
                    sum=sum+self.rateBoard(self.getSubBoard(i),player)
                elif self.mainBoardMatrix[r,c]==player:
                    sum=sum+3

            return sum+18*self.rateBoard(self.mainBoardMatrix,player)

    def rateBoard(self, board, player):
        val = 0
        val = val + self.isAlmostWon(board[1,:], player)
        val = val + self.isAlmostWon(board[2,:], player)
        val = val + self.isAlmostWon(board[0,:], player)
        val = val + self.isAlmostWon(board[:,1], player)
        val = val + self.isAlmostWon(board[:,2], player)
        val = val + self.isAlmostWon(board[:,0], player)
        val = val + self.isAlmostWon(numpy.array([board[1, 1], board[2, 2], board[0, 0]]), player)
        val = val + self.isAlmostWon(numpy.array([board[2,0], board[1,1], board[0, 2]]), player)

        if val > 0:
            val = 1

        return val

    def isAlmostWon(self, a, player):

        if sum(numpy.equal(a, player*numpy.ones(a.shape)))==2 and sum(numpy.equal(a, numpy.zeros(a.shape)))==1 :
            return 1
        else:
            return 0

    def printBoard(self):

        for c in range(0,9):
            for r in range(0,9):
                print(int(self.boardMatrix[r,c]), end="")
                if r%3==2 and not r==8:
                    print("  |  ", end="")
            print()

            if c % 3 == 2 and not c == 8:
                print("----------------")

    def isWon(self, board):

        if self.isAllSame(board[1,: ]):
            return True
        elif self.isAllSame(board[2,:]):
            return True
        elif self.isAllSame(board[0,:]):
            return True
        elif self.isAllSame(board[:,1]):
            return True
        elif self.isAllSame(board[:,2]):
            return True
        elif self.isAllSame(board[:,0]):
            return True
        elif self.isAllSame(numpy.array([board[1,1], board[2,2], board[0,0]])):
            return True
        elif self.isAllSame(numpy.array([board[2,0], board[1,1], board[0,2]])):
            return True
        else:
            return False

    def whoIsWinner(self):
        # returns 0 if no one is winner, or player id of winner
        if self.isAllSame(self.mainBoardMatrix[1,: ]):
            return self.mainBoardMatrix[1,0]
        elif self.isAllSame(self.mainBoardMatrix[2,:]):
            return self.mainBoardMatrix[2,0]
        elif self.isAllSame(self.mainBoardMatrix[0,:]):
            return self.mainBoardMatrix[0,0]
        elif self.isAllSame(self.mainBoardMatrix[:,1]):
            return self.mainBoardMatrix[0,1]
        elif self.isAllSame(self.mainBoardMatrix[:,2]):
            return self.mainBoardMatrix[0,2]
        elif self.isAllSame(self.mainBoardMatrix[:,0]):
            return self.mainBoardMatrix[0,0]
        elif self.isAllSame(numpy.array([self.mainBoardMatrix[1,1], self.mainBoardMatrix[2,2], self.mainBoardMatrix[0,0]])):
            return self.mainBoardMatrix[1,1]
        elif self.isAllSame(numpy.array([self.mainBoardMatrix[2,0], self.mainBoardMatrix[1,1], self.mainBoardMatrix[0,2]])):
            return self.mainBoardMatrix[2,0]
        else:
            return 0

    def isAllSame(self,a):
        if a[1]==a[0] and a[2]==a[1] and not a[0] ==0:
            return True
        else:
            return False

    def getAllMoves(self):
        moves=[]
        rb=self.lastBoard %3
        cb=math.floor(self.lastBoard/3)
        if self.mainBoardMatrix[rb,cb]==0:
            for r in range(0,3):
                for c in range(0,3):
                    if self.getSubBoard(self.lastBoard)[r,c] == 0:
                        moves.append(Move(self.whoseTurn, 3 * cb + rb, 3*c+r))
        else:
            for rb in range(0, 3):
                for cb in range(0, 3):
                    if self.mainBoardMatrix[rb, cb] == 0:
                        for r in range(0, 3):
                            for c in range(0, 3):
                                if self.getSubBoard(3*cb+rb)[r, c] == 0:
                                    moves.append(Move(self.whoseTurn, 3 * cb + rb, 3 * c + r))
        random.shuffle(moves)
        return moves

    def __copy__(self):
        copy = Board(self.whoseTurn)
        copy.boardMatrix = self.boardMatrix.copy()
        copy.mainBoardMatrix = self.mainBoardMatrix.copy()
        copy.isGameOver = self.isGameOver
        copy.lastBoard = self.lastBoard
        return copy

    def getBoardTensor(self):
        boardTensor=numpy.zeros((3,3,3,3))
        for ro in range(3):
            for co in range(3):
                for ri in range(3):
                    for ci in range(3):
                        boardTensor[ro, co, ri, ci]=self.boardMatrix[3 * ro + ri, 3 * co + ci]
        return boardTensor
    def getValidMoves(self):
        boardTensor=numpy.zeros((3,3,3,3),dtype=bool)
        rb=self.lastBoard %3
        cb=math.floor(self.lastBoard/3)
        if self.mainBoardMatrix[rb,cb]==0:
            for r in range(0,3):
                for c in range(0,3):
                    if self.getSubBoard(self.lastBoard)[r,c] == 0:
                        boardTensor[rb,cb,r,c]=True
        else:
            for rb in range(0, 3):
                for cb in range(0, 3):
                    if self.mainBoardMatrix[rb, cb] == 0:
                        for r in range(0, 3):
                            for c in range(0, 3):
                                if self.getSubBoard(3*cb+rb)[r, c] == 0:
                                    boardTensor[rb,cb,r,c]=True
        return boardTensor

