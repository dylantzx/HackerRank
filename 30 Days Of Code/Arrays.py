############################# Question ###########################

# https://www.hackerrank.com/challenges/30-arrays/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

def printReverseArray(arr):
    print(*arr[::-1])

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    printReverseArray(arr)
    