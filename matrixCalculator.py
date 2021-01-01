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
    x.replace(2,0,1)
    x. scale(2,1)
    x.switch(0,1)
    x.printREFMatrix()
    number = Fraction(3.5)
    print(number.numerator)
    print(number.denominator)


##This is the matrix class, it will hold the different form that the calcuator will find
##The algorithim for finding ithe forms wil be done in the main
class Matrix:
    def __init__(self,row,col, entries):
        self.rowSize = row
        self.colSize = col
        self.colIndex = col-1
        self.rowIndex = row-1
        self.mainMatrix = np.array(entries).reshape(self.rowSize, self.colSize)
        self.REFMatrix = np.array(entries).reshape(self.rowSize, self.colSize)
        self.storageMatrix = np.array(entries).reshape(self.rowSize, self.colSize)
    
    def printMainMatrix(self):
        for x in range(0, self.rowSize):
            for y in range(0,self.colSize):
                if(y == self.colSize-1):
                    print(Fraction(self.mainMatrix[x][y]), sep='   ', end='\n')
                else:
                    print(Fraction(self.mainMatrix[x][y]), sep='   ', end= ' ')
    
    def printREFMatrix(self):
        for x in range(0, self.rowSize):
            for y in range(0,self.colSize):
                if(y == self.colSize-1):
                    print(Fraction(self.REFMatrix[x][y]), sep='   ', end='\n')
                else:
                    print(Fraction(self.REFMatrix[x][y]), sep='   ', end= ' ')

    def replace(self, scale, rA, rB):
        self.REFMatrix[rA] = self.REFMatrix[rA]+scale*self.REFMatrix[rB]

    def scale(self, scale, row):
        self.REFMatrix[row] = scale*self.REFMatrix[row]

    def switch(self, rA, rB):
        self.storageMatrix[0] =  self.REFMatrix[rA]
        self.REFMatrix[rA] =  self.REFMatrix[rB]
        self.REFMatrix[rB] = self.storageMatrix[0]


    


##def  findREF(matrix):





        



main()