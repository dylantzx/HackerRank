############################# Question ###########################

# https://www.hackerrank.com/challenges/30-binary-numbers/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

def countMaxConsecutives(n):
    binaryNum = bin(n)[2:]
    consecutiveList = binaryNum.split('0')
    longestConsecutive = len(max(consecutiveList))
    print(longestConsecutive)

if __name__ == '__main__':
    n = int(input())
    countMaxConsecutives(n)
