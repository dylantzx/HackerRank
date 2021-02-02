############################# Question ###########################

# https://www.hackerrank.com/challenges/the-birthday-bar/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    sum_of_block = []
    # Using sliding window approach, add each consecutive block into an array
    for i in range(len(s)):
        sum_of_block.append(sum(s[i:m+i]))
    # Creates a list containing 1s if a block==d then return the sum of 1s
    return sum([sum_of_block[block]==d for block in range(len(sum_of_block))])
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
