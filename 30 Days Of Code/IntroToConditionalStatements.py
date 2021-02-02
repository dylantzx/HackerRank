############################# Question ###########################

# https://www.hackerrank.com/challenges/30-conditional-statements/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

def weird(N):
    print("Weird" if N%2!=0 or (N%2==0 and 6<=N<=20) else "Not Weird")
    
if __name__ == '__main__':
    N = int(input())
    weird(N)
