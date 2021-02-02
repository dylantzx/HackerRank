############################# Question ###########################

# https://www.hackerrank.com/challenges/30-operators/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total = round(meal_cost + (meal_cost * (tip_percent + tax_percent)/100))
    print(int(total))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
