#First we are gonna get the user to build a matrix easy right?
#So second we are going to implement the three row operations Replacement, Switching, Scaling
import math
import sys
import os
import vEnv39
import numpy as np

def main():
    rowSize, colSize = input("Please enter your matrix size (ex. 3,4 for a 3x4 matrix): ").split(",")
    print("Enter your matrix values as a single line, left to right, row 0 to row x")
    entries = list(map(int, input().split()))
    mainMatrix = np.array(entries).reshape(rowSize, colSize)
    print(*mainMatrix, sep='    ')




main()