
############################# Question ###########################

# https://www.hackerrank.com/challenges/30-2d-arrays/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(arr):
    NumOfRows = len(arr) #6
    NumOfCols = len(arr[0]) #6
    hourglassList = []
    for rows in range(NumOfRows-2):
        hourglassValue=0
        for cols in range(NumOfCols-2):
            # print(rows, cols)
            hourglassValue = sum(arr[rows][cols:cols+3]) + arr[rows+1][cols+1]+ sum(arr[rows+2][cols:cols+3])
            hourglassList.append(hourglassValue)
    
    print(max(hourglassList))

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourglass(arr)