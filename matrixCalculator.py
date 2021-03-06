##Matrix Row Reduction Calculator
##Date: Winter 2020
##Author: Michael Dorado
##Description: This calculator will take in a users input and conert it to a matrix of which it can calculate the 
##REF and RREF
import math
import sys
import os
import vEnv39
import numpy as np
from fractions import Fraction

def main():
    rowSize, colSize = list(map(int,input("Please enter your matrix size (ex. 3,4 for a 3x4 matrix): ").split(",")))##Need to put error catcher here
    entries = list(map(float, input("Enter your matrix values as a single line, left to right, row 0 to row x: ").split()))##Need to put error catcher here
    x = Matrix(rowSize,colSize,entries)
    x.printMainMatrix()
    ##x.replace(2,0,1)
    ##x. scale(2,1)
    ##x.switch(0,1)
    x.printRREFMatrix()
    number = Fraction(3.5)
    print(number)
    print(number.numerator)
    print(number.denominator)
    findREF(x)

##This is the matrix class, it will hold the different form that the calcuator will find
##The algorithim for finding ithe forms wil be done in the main
class Matrix:
    def __init__(self,row,col, entries):
        self.pivotColCount = 1
        self.rowSize = row
        self.colSize = col
        self.colIndex = col-1
        self.rowIndex = row-1
        self.mainMatrix = np.array(entries).reshape(self.rowSize, self.colSize)
        self.RREFMatrix = np.array(entries).reshape(self.rowSize, self.colSize)
        self.storageMatrix = np.array(entries).reshape(self.rowSize, self.colSize)
    
    def printMainMatrix(self):
        for x in range(0, self.rowSize):
            for y in range(0,self.colSize):
                if(y == self.colSize-1):
                    print(Fraction(self.mainMatrix[x][y]).limit_denominator(1000), sep='   ', end='\n')
                else:
                    print(Fraction(self.mainMatrix[x][y]).limit_denominator(1000), sep='   ', end= ' ')
    
    def printRREFMatrix(self):
        for x in range(0, self.rowSize):
            for y in range(0,self.colSize):
                if(y == self.colSize-1):
                    print(Fraction(self.RREFMatrix[x][y]).limit_denominator(1000), sep='   ', end='\n')
                else:
                    print(Fraction(self.RREFMatrix[x][y]).limit_denominator(1000), sep='   ', end= ' ')

    def replace(self, scale, rA, rB):
        self.RREFMatrix[rA] = self.RREFMatrix[rA]+scale*self.RREFMatrix[rB]

    def scale(self, scale, row):
        self.RREFMatrix[row] = scale*self.RREFMatrix[row]

    def switch(self, rA, rB):
        self.storageMatrix[0] =  self.RREFMatrix[rA]
        self.RREFMatrix[rA] =  self.RREFMatrix[rB]
        self.RREFMatrix[rB] = self.storageMatrix[0]
    
    def findScale(self, row, col):
        return self.RREFMatrix[row][col]
    
    def checkZeroRow(self,row):
        isZeroRow = True
        for y in range(0, self.colSize): ##This is how we are going to account for zero rows atm, but I want functionality added so that the user may select whether they are solving the right hand side or just reducing a matrix
            if(self.RREFMatrix[row][y] != 0):
                isZeroRow = False
        return isZeroRow
    
    def checkPivotCol(self,col):
        isPivotCol = False
        leadingEntryOne = False
        leadingEntryFlag = False
        for x in range(0,self.rowSize):
            if(self.RREFMatrix[x][col] == 1):
                leadingEntryOne = True
            if(leadingEntryOne == True):
                isPivotCol = True
                for y in range(x+1, self.rowSize):
                    if(self.RREFMatrix[y][col] != 0):
                        isPivotCol = False
                return isPivotCol

    def numberOfZeroRow(self):
        counter = 0
        for x in range(0, self.rowSize):
            if(self.checkZeroRow(x) == True):
                counter += 1
        return counter

    def pivotColCount(self):
        counter = 0
        for x in range(0,self.colSize):
           if(self.checkPivotCol(x) == True):
               count += 1
        return counter
        
    def lowerTriangleZero(self):
        zeroRowCount = self.numberOfZeroRow()







    
def  findREF(matrix):
    xIndex = 0
    yIndex = 0
    ##while(matrix.numberOfZeroRow() + numberOfLeadingEntry() == matrix.rowIndex and matrix.lowerTriangleZero() == True ): ##Functions to be built
    moveZeroRows(matrix)
    print(matrix.checkPivotCol(0))

def moveZeroRows(matrix):
    for x in range(0, matrix.rowSize):
        if(matrix.checkZeroRow(x) == True):
            zeroShuffle = matrix.rowIndex
            while (zeroShuffle > x and matrix.checkZeroRow(zeroShuffle)  ==  True):
                zeroShuffle -= 1
            matrix.switch(x, zeroShuffle)
main()