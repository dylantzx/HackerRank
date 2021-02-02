############################# Question ###########################

# https://www.hackerrank.com/challenges/compare-the-triplets/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    s1,s2 = 0,0
    print(a,b)
    for i,j in zip(a,b):
        if i>j:
            s1+=1
        elif i<j:
            s2+=1
    return [s1,s2]   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

