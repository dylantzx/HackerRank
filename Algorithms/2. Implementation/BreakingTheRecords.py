############################# Question ###########################

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowest= [scores[0]]
    best = [scores[0]]
    for score in range(1,len(scores)):
        if scores[score] > best[-1]:
            best.append(scores[score])
        elif scores[score] < lowest[-1]:
            lowest.append(scores[score])
    return len(best)-1,len(lowest)-1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
