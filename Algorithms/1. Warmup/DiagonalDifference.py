############################# Question ###########################

# https://www.hackerrank.com/challenges/diagonal-difference/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diag_counter=0
    l_t_r = 0
    r_t_l = 0
    for i in range(1,len(arr)+1):
        l_t_r += arr[i-1][diag_counter]
        r_t_l += arr[-i][diag_counter]
        diag_counter+=1
    return abs(l_t_r - r_t_l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
