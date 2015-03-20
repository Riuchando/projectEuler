#!/usr/bin/env python
import random
from random import randint
import time
import math
from math import sqrt
import copy


#########################
# Helper functions
########################

def rawRead( filename ):
    ''' cheat for reading in files '''
    file = open(filename,'r')
    raw = file.read()
    file.close()
    return raw

class MyGame(object):

    def __init__(self, gameData):
        #self.board = gameData
        self.boardMap = {}
        self.ansMap = {}
        for i in range(9):
            for j in range(9):
                self.boardMap[(i,j)] = gameData[i][j]
                if( gameData[i][j] == '0' ):
                    self.ansMap[(i,j)] = '123456789'
                else:
                    self.ansMap[(i,j)] = ''
   
    def print(self):
        s = ''
        for i in range(9):
            for j in range(9):
                s += self.boardMap[(i,j)] + " "
                if( j == 2 or j == 5 ):
                    s += "|"
                elif( j == 8 ):
                    s += "\n"
            if( i == 2 or i == 5 ):
                s += "------+------+------\n"
        print(s)
                
    def boxRow(self,row,col):
        ''' returns the box row containing row, col '''
        return (row//3)*3 + (col//3)
    
    def remove(self, n, i, j):   # remove(value, row, col)
        if( self.ansMap[(i,j)].find(n) < 0 ):  # not found
            return False
        else:
            self.ansMap[(i,j)] = self.ansMap[(i,j)][:self.ansMap[(i,j)].find(n)] + self.ansMap[(i,j)][self.ansMap[(i,j)].find(n)+1:]
            return True

    def reduceBox(self, n , x, y):
        ''' reduce a 3x3 box of coordinates starting at upper left corner (i,j) '''
        for i in range(x,x+3):
            for j in range(y,y+3):
                self.remove(n,i,j)

    def updateBoard(self):
        ''' we will walk the self.ansMap and update the board map as needed '''
        numberUpdated = 0
        for i in range(9):
            for j in range(9):
                if( len(self.ansMap[(i,j)]) == 1 ):  # only one possible answer remains
                    numberUpdated += 1
                    self.boardMap[(i,j)] = self.ansMap[(i,j)]  # board = remaining solution
                    self.ansMap[(i,j)] = ''                    # clear answer
        return numberUpdated

    def checkRowForUnique(self):
        for n in '123456789':   # for each number
            for i in range(9):
                foundCount = 0
                foundAt = (-1,-1)
                for j in range(9):  # checking row, moving across ->
                    if( n in self.ansMap[(i,j)] ):   # if we find this number...
                        foundCount += 1
                        foundAt = (i,j)
                # after we finish sweeping the row...
                if( foundCount == 1 ):          # if exactly one 'n' exists in this row...
                    #print("found unique",n,'at',foundAt)
                    self.ansMap[foundAt] = n   # clear this ansMap (solution is found!)
                    #self.boardMap[foundAt] = n  # correct game board
        return

    def checkColForUnique(self):
        for n in '123456789':   # for each number
            for j in range(9):
                foundCount = 0
                foundAt = (-1,-1)
                for i in range(9):  # checking row, moving across ->
                    if( n in self.ansMap[(i,j)] ):   # if we find this number...
                        foundCount += 1
                        foundAt = (i,j)
                # after we finish sweeping the row...
                if( foundCount == 1 ):          # if exactly one 'n' exists in this row...
                    #print("found unique",n,'at',foundAt)
                    self.ansMap[foundAt] = n   # clear this ansMap (solution is found!)
                    #self.boardMap[foundAt] = n  # correct game board
        return

    def checkBoxForUnique(self):
        for n in '123456789':   # for each number
            for x in range(3):      
                for y in range(3):
                    foundCount = 0
                    foundAt = (-1,-1)
                    for i in range(3*(x//3),3*(x//3)+3):      # checking each small subox
                        for j in range(3*(y//3),3*(y//3)+3):
                            if( n in self.ansMap[(i,j)] ):   # if we find this number...
                                foundCount += 1
                                foundAt = (i,j)
                    # after we finish sweeping the box...
                    if( foundCount == 1 ):          # if exactly one 'n' exists in this box...
                        #print("found unique",n,'at',foundAt)
                        self.ansMap[foundAt] = n   # clear this ansMap (solution is found!)
        

    def reduce(self):
        ''' we will walk the self.boardMap and remove from self.ansmap '''
        totalUpdates = 0
        ##------------------------------------------------------##
        ##  Step 1: eliminate Row / Col / Box  solution overlaps
        ##------------------------------------------------------##
        for i in range(9):
            for j in range(9):
                if( self.boardMap[(i,j)] != '0' ):  # if a solution exists
                    # then we will wipe out this number from this row, column, and box
                    row = i
                    col = j
                    n = self.boardMap[(i,j)]
                    for index in range(9):
                        self.remove(n,index,col)  # remove n from all indexes of this column
                        self.remove(n,row,index)  # remove n from all indexes of this row
                    # TODO: still need to clear the individual boxes...
                    self.reduceBox(n,3*(row//3),3*(col//3))

        ## Solved 12 of 50 with above algorithm...

        ##---------------------------------------------------------##
        ##  Step 2: look for isolated solutions per row / col / box
        ##---------------------------------------------------------##

        self.checkRowForUnique()
        # Solved 21 of 50 with above algorithm...

        self.checkColForUnique()
        # Solved 39 of 50 with above algorithm...

        self.checkBoxForUnique()
        # Solved 40 of 50 with above algorithm...

        # at the end, update the Board
        totalUpdates += self.updateBoard()
        return totalUpdates

    def solved(self):
        ''' check to see if board is solved '''
        for i in range(9):
            for j in range(9):
                if( self.boardMap[(i,j)] == '0' ):
                    return False
        return True

    def verify(self):
        ''' loose verification to check if solution is valid '''
        for i in range(9):
            sumRow = 0
            sumCol = 0
            for j in range(9):
                sumRow += int(self.boardMap[(i,j)])
                sumCol += int(self.boardMap[(j,i)])
            if( sumRow != 45 or sumCol != 45 ):
                return False
        return True
            

    def solve(self):
        ''' attempt to solve the board '''
        while( self.reduce() ):
            # wait for reduction to fail...
            pass
        if( self.solved() and self.verify() ):
            return True
        else:
            return False

    def gsolve(self):
        ''' attempt 100 guesses to solve the board '''
        attempts = 100
        while( attempts > 0 ):
            if( self.guessSolve() ):   # if we solve it successfully
                return True
            else:
                attempts -= 1
        return False            # after 100 attempts give up

    def guessSolve(self):
        # if already solved, just return True (safety)
        if( self.solved() ):
            return True
        
        # if guess solve fails, we need to restore backup
        boardMap_bu = copy.deepcopy(self.boardMap)
        ansMap_bu = copy.deepcopy(self.ansMap)
        
        # count # of unsolved digits
        zeroCount = 0
        for i in range(9):
            for j in range(9):
                if self.boardMap[(i,j)] == '0':  # if unsolved...
                    zeroCount += 1
        randomIndex = randint(0,zeroCount-1)  # this is the index we will try to guess
        for i in range(9):
            for j in range(9):
                if self.boardMap[(i,j)] == '0':
                    randomIndex -= 1
                    if( randomIndex < 1 ):
                        myGuessIndex = randint(0,len(self.ansMap[(i,j)])-1)
                        myGuess = self.ansMap[(i,j)][myGuessIndex]
                        #print("Guessing:",myGuess,"for",i,j)
                        self.ansMap[(i,j)] = myGuess
                        randomIndex = 999   # only guess once!

        #Now that we made a guess, try to solve regularly...
        if( self.solve() ):   # if our guess solves the puzzles...
            return True
        else:                 # our guess failed, we need to restore backup data
            self.boardMap = copy.deepcopy(boardMap_bu)
            self.ansMap = copy.deepcopy(ansMap_bu)
            return False

    def getKey(self):
        ''' returns three digit int needed to solve pe96 problem '''
        key = self.boardMap[(0,0)] + self.boardMap[(0,1)] + self.boardMap[(0,2)]
        return int(key)

    def dbans(self):
        for i in range(9):
            for j in range(9):
                if( self.ansMap[(i,j)] != '' ):
                    print("(" + str(i) + "," + str(j) + ")","-", self.ansMap[(i,j)])



        
def pe96():
    # Su Doku
    raw = rawRead('p096_sudoku.txt')
    ''' will load games later ...'''

    # game will be stored in following structure:
    games = []  # collection of 'game' type
    game = []
    buff = ''
    lines = 1
    for c in raw:
        if( c == '\n' ):
            if( 'Grid' in buff ):
                lines = 1    # flag for new game
                buff = ''
            else:
                if( lines == 9 ):
                    game.append(buff)
                    games.append(game)
                    buff = ''
                    game = []
                else:
                    game.append(buff)
                    buff = ''
                    lines += 1
        else:
            buff += c


    
    # now we have an array of game data.  Time to solve
    solved = 0
    counter = 0
    pe96sum = 0
    gameObjects = []
    for data in games:
        g = MyGame(data)  # create an instance of game
        gameObjects.append(g)

        print('Game',counter,end="")
        if( g.solve() ):
            print("  - solved")
            solved += 1
            pe96sum += g.getKey()
        else:
            if( g.gsolve() ):
                print(" - gsolved")
                solved += 1
                pe96sum += g.getKey()
            else:
                print("  - stuck")
        counter += 1
        
    print("\nSolved a total of",solved,"games")
    print("Sum =",pe96sum)
    
            
    return gameObjects

    
if __name__ == '__main__':
    print("GO")
    out = pe96()

