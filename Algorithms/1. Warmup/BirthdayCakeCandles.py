############################# Question ###########################

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
# Attempting to solve this solution via divide and conquer method
def birthdayCakeCandles(candles):
    ls = []
    divAndConq(candles, ls)
    return len(ls)
    
def divAndConq(candles, ls):
    
    if len(candles)>1:
        middle = math.floor(len(candles)/2)
        divAndConq(candles[:middle], ls)
        divAndConq(candles[middle:], ls)
    else:
        if len(ls) == 0:
            ls.append(candles[0])
        else:
            if candles[0] < ls[0]:
                return
            elif candles[0] == ls[0]:
                ls.append(candles[0])
            else:
                ls.clear()
                ls.append(candles[0])
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
