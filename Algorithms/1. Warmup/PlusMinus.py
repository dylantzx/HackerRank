############################# Question ###########################

# https://www.hackerrank.com/challenges/plus-minus/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=0
    n=0
    z=0
    total = len(arr)
    for num in arr:
        if num>0:
            p+=1
        elif num==0:
            z+=1
        else:
            n+=1
    print(round(p/total,6))
    print(round(n/total,6))
    print(round(z/total,6))
    
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
