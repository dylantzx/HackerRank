############################# Question ###########################

# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

##################################################################
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs_dict = {}
    pairs = 0
    for sock in ar:
        count = ar.count(sock)
        if sock not in pairs_dict:
            pairs_dict[sock] = count
    for value in pairs_dict.values():
        if value%2 == 0:
            pairs+= value/2
        else:
            pairs+= (value-1)/2
    return int(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
