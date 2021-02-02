############################# Question ###########################

# https://www.hackerrank.com/challenges/mini-max-sum/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    temp_list = []
    for i in range(len(arr)):
        curr_sum = sum(arr[:])-arr[i]
        temp_list.append(curr_sum)
    print(f"{min(temp_list)} {max(temp_list)}")
    
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
