############################# Question ###########################

# https://www.hackerrank.com/challenges/migratory-birds/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds_dic = {}
    for type_of_birds in arr:
        birds_dic[type_of_birds] = birds_dic.get(type_of_birds, 0)+1

    max_value = max(birds_dic.values())
    max_list = [key for key, value in birds_dic.items() if value==max_value]
    return min(max_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
