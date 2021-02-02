############################# Question ###########################

# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

##################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    calendar = [31,28,31,30,31,30,31,31,30,31,30,31]
    daysInyear = [sum(calendar[:month+1]) for month in range(len(calendar))]
    leap = checkLeapYear(year)
    date = []
    for days in daysInyear[::-1]:
        if days < 256:
            day_count = 256 - days
            if leap ==1:
                day_count -=1
            elif leap ==2:
                day_count = 256 + 13 - days
            date.append(day_count)
            date.append(daysInyear.index(days)+2)
            date.append(year)
            break
    if date[1]<10:
        date_str =f"{date[0]}.0{date[1]}.{date[2]}"
    else:
        date_str = f"{date[0]}.{date[1]}.{date[2]}"
    return date_str
        
def checkLeapYear(year):
    leap = 0
    if 1700<=year<=1917 and year%4 ==0:
        leap = 1
    elif year>=1919 and (year%400==0 or (year%4==0 and year%100!=0)):
        leap = 1
    elif year==1918:
        leap = 2
    return leap    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
