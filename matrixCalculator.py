#First we are gonna get the user to build a matrix easy right?
#So second we are going to implement the three row operations Replacement, Switching, Scaling
import math
import sys
import os
import vEnv39
import numpy as np

def main():
    rowSize, colSize = list(map(int,input("Please enter your matrix size (ex. 3,4 for a 3x4 matrix): ").split(",")))
    entries = list(map(int, input("Enter your matrix values as a single line, left to right, row 0 to row x: ").split()))
    x = Matrix(rowSize,colSize,entries)
    x.printMainMatrix()
    x.replace(2,1,2)
    x.printMainMatrix()

class Matrix:
    def __init__(self,row,col, entries):
        self.rowSize = row
        self.colSize = col
        self.mainMatrix = np.array(entries).reshape(self.rowSize, self.colSize)
        self.REFMatrix = np.array(entries).reshape(self.rowSize, self.colSize)
        self.RREFMatrix = np.array(0).reshape(self.rowSize, self.colSize)
    
    def printMainMatrix(self):
        for x in range(0, self.rowSize):
            for y in range(0,self.colSize):
                if(y == self.colSize-1):
                    print(self.mainMatrix[x][y], sep='   ', end='\n')
                else:
                    print(self.mainMatrix[x][y], sep='   ', end= ' ')
    
    def replace(self, scale, rA, rB):
        for x in range(0,self.colSize):
            self.matrix[rA] = self.matrix[rA]+scale*self.matrix[rB]



        



main()