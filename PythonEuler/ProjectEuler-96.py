#!/usr/bin/env python
import random
import time
import math
from math import sqrt


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
        self.board = gameData

        self.solutionMatrix = []
        emptyArray = []
        for i in range(9):
            emptyArray.append([])
        for i in range(9):
            self.solutionMatrix.append(list(emptyArray))
        for i in range(9):
            for j in range(9):
                if( self.p(i,j) == '0' ):
                    self.solutionMatrix[i][j] = '123456789'
                else:
                    self.solutionMatrix[i][j] = self.p(i,j)
        
        ''' create row data '''
        self.virtualRow = ['','','','','','','','','']
        self.virtualCol = ['','','','','','','','','']
        self.rowData = []
        for row in self.board:
            self.rowData.append(row)
        ''' create col data '''
        self.colData = []
        row = ''
        for i in range(9):
            for j in range(9):
                row += self.board[j][i]
            self.colData.append(row)
            row = ''
        ''' create box data '''
        self.boxData = []
        for j in range(3):
            self.boxData.append(self.board[0+j*3][0:3]+
                                self.board[1+j*3][0:3]+
                                self.board[2+j*3][0:3])
            self.boxData.append(self.board[0+j*3][3:6]+
                                self.board[1+j*3][3:6]+
                                self.board[2+j*3][3:6])
            self.boxData.append(self.board[0+j*3][6:9]+
                                self.board[1+j*3][6:9]+
                                self.board[2+j*3][6:9])                

    def updateCheckData(self):
        self.rowData = []
        for row in self.board:
            self.rowData.append(row)
        ''' create col data '''
        self.colData = []
        row = ''
        for i in range(9):
            for j in range(9):
                row += self.board[j][i]
            self.colData.append(row)
            row = ''
        ''' create box data '''
        self.boxData = []
        for j in range(3):
            self.boxData.append(self.board[0+j*3][0:3]+
                                self.board[1+j*3][0:3]+
                                self.board[2+j*3][0:3])
            self.boxData.append(self.board[0+j*3][3:6]+
                                self.board[1+j*3][3:6]+
                                self.board[2+j*3][3:6])
            self.boxData.append(self.board[0+j*3][6:9]+
                                self.board[1+j*3][6:9]+
                                self.board[2+j*3][6:9])
    
    def printBoard(self):
        # nicely formatted print of current board state
        skip = 0
        for row in self.board:
            if( skip == 3 or skip == 6):
                print("---+---+---")
                print(row[0:3] + "|" + row[3:6] + "|" + row[6:9])
                skip += 1
            else:
                print(row[0:3] + "|" + row[3:6] + "|" + row[6:9])
                skip += 1

    def checkBoard(self):
        for row in self.rowData:
            for c in '123456789':   # test set
                if( row.count(c) > 1 ):
                    return False
        for row in self.colData:
            for c in '123456789':
                if( row.count(c) > 1 ):
                    return False
        for row in self.boxData:
            for c in '123456789':
                if( row.count(c) > 1 ):
                    return False
        # else
        return True

    def checkSolved(self):
        for i in range(9):
            for j in range(9):
                if(self.p(i,j) == '0'):
                    return False
        return True
                

    ''' Getter helper function '''
    def p(self,row,col):
        return self.board[row][col]

    def boxRow(self,row,col):
        ''' returns the box row containing row, col '''
        return (row//3)*3 + (col//3)

    def remove(self, value, s):
        if( s.find(value) < 0 ):  # not found
            return s
        else:
            return s[:s.find(value)] + s[s.find(value)+1:]

    def change(self, row, col, value):
        self.board[row] = self.board[row][0:col] + value + self.board[row][col+1:]

    def eliminate(self):
        ''' works through every item in game board and searches for correct answer '''
        changedFlag = False
        for i in range(9):      #row
            for j in range(9):  #column
                if( self.p(i,j) == '0' ):   # if spot isn't solved yet
                    possible = '123456789'  # Answer key - we will remove items
                    for n in '123456789':   # for each of the nine digits
                        if n in self.rowData[i]:
                            possible = self.remove(n, possible)
                        if n in self.colData[j]:
                            possible = self.remove(n, possible)
                        if n in self.boxData[self.boxRow(i,j)]:
                            possible = self.remove(n, possible)
                    if( len(possible) == 1 ):  # only one possible answer left!
                        #print("!!!",i,j,possible)
                        self.change(i,j,possible)
                        changedFlag = True
        if( changedFlag ):
            self.updateCheckData()
        return changedFlag

    def eliminateRow(self):
        ''' look for '0' in a row, and check to see how many will fit a number '''
        changedFlag = False
        for n in '123456789':       #check to see if each number would fit
            count = 0               #count number of places a fit occurs
            spot  = (-1,-1,-1)      # row, col, num
            for i in range(9):      #row
                for j in range(9):  #col
                    if(self.p(i,j) == '0'):
                        if(n not in self.rowData[i] and
                           n not in self.colData[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            count += 1
                            spot = (i,j,n)
                # after checking each col...
                if count == 1:
                    #print("--x",spot)
                    self.change(spot[0],spot[1],spot[2])
                    changedFlag = True
                    #self.updateCheckData()
                count = 0

        if( changedFlag ):
            self.updateCheckData()  
        return changedFlag


    def eliminateCol(self):
        ''' look for '0' in a column, and check to see how many will fit a number '''
        changedFlag = False
        for n in '123456789':       #check to see if each number would fit
            count = 0               #count number of places a fit occurs
            spot  = (-1,-1,-1)      # row, col, num
            for j in range(9):      #col
                for i in range(9):  #row
                    if(self.p(i,j) == '0'):
                        if(n not in self.rowData[i] and
                           n not in self.colData[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            count += 1
                            spot = (i,j,n)
                # after checking each row...
                if count == 1:
                    #print("||x",spot)
                    self.change(spot[0],spot[1],spot[2])
                    changedFlag = True
                    #self.updateCheckData()
                count = 0

        if( changedFlag ):
            self.updateCheckData()
        return changedFlag

                            

    def eliminateBox(self):
        changedFlag = False
        for n in '123456789':      # try each run of boxes with all numbers
            
            count = 0
            spot  = (-1,-1,-1)      # row, col, num
            
            # not sure how to frame the algorithm (and it's late) so going to brute force it first
            for i in range(0,3):
                for j in range(0,3):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num
            
            for i in range(0,3):
                for j in range(3,6):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num
            
            for i in range(0,3):
                for j in range(6,9):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num

            for i in range(3,6):
                for j in range(0,3):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num

            for i in range(3,6):
                for j in range(3,6):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num

            for i in range(3,6):
                for j in range(6,9):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num

            for i in range(6,9):
                for j in range(0,3):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num

            for i in range(6,9):
                for j in range(3,6):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num

            for i in range(6,9):
                for j in range(6,9):
                    if( self.p(i,j) == '0' ):
                        if(n not in self.rowData[i] and n not in self.virtualRow[i] and
                           n not in self.colData[j] and n not in self.virtualCol[j] and
                           n not in self.boxData[self.boxRow(i,j)]):
                            lastspot = spot   # copy old spot over
                            count += 1
                            spot = (i,j,n)
                            
            if count == 1:
                self.change(spot[0],spot[1],spot[2])
                changedFlag = True
                #print("[]x",spot)
            elif count == 2:   # test for a virtual number
                if( spot[0] == lastspot[0] ):  # same rows...
                    self.virtualRow[spot[0]] += n
                    print("Added",n,"to virtual Row",spot[0])
                elif( spot[1] == lastspot[1] ): # same cols...
                    self.virtualCol[spot[1]] += n
                    print("Added",n,"to virtual Col",spot[1])
                
            count = 0
            spot  = (-1,-1,-1)      # row, col, num

        if( changedFlag ):
            self.updateCheckData()
        return changedFlag
                
    def solve(self):
        notStuck = True
        while( notStuck ):
            notStuck = False
            notStuck |= self.eliminate()
            notStuck |= self.eliminateRow()
            notStuck |= self.eliminateCol()
            notStuck |= self.eliminateBox()
        if( self.checkSolved() ):
            print("Solved!")
            self.printBoard()
            return True
        else:
            print("We are stuck")
            self.printBoard()
            return False
          



def change(s, idx, value):
    ''' s = row string, idx = index to change, value = string value '''
    s = s[0:idx] + value + s[idx+1:]
    return s

        
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
    gameObjects = []
    for data in games:
        g = MyGame(data)  # create an instance of game
        gameObjects.append(g)
    '''
        print('\n Game',counter)
        g.printBoard()
        if( g.solve() ):
            solved += 1
        counter += 1
    '''    
    print("\nSolved a total of",solved,"games")        
    
            
    return gameObjects

    
if __name__ == '__main__':
    print("GO")
    out = pe96()

