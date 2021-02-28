
############################# Question ###########################

# https://www.hackerrank.com/challenges/30-regex-patterns/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

def printName(name_list):
    # print(firstName, emailID)
    sorted_list = sorted(name_list)
    print(*sorted_list, sep="\n") 

if __name__ == '__main__':
    N = int(input())
    mail = "@gmail.com"
    name_list = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if mail in emailID:
            name_list.append(firstName)
    printName(name_list)
