############################# Question ###########################

# https://www.hackerrank.com/challenges/time-conversion/problem

##################################################################

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    # Scenarios:
    # 1) 12AM -> 00:00 (-12hrs)
    if s[:2] == '12' and s[-2] == 'A':
        return '00' + s[2:-2]
    # 2) 1PM - 11PM -> 13:00- 23:00 (+12hrs)
    elif int(s[:2]) >=1 and int(s[:2]) <=11 and s[-2] == 'P':
        return str(int(s[:2])+12) + s[2:-2]
    # 3) 1AM - 12PM -> Not much changes (only exclude the AM/PM)
    else:
        return s[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
