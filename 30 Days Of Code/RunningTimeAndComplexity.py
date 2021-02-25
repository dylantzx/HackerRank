############################# Question ###########################

# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

##################################################################

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

times = int(input())
for i in range(times):
    prime = True
    number = int(input())
    sr = int(sqrt(number))
    if number == 1:
        prime = False
    else:
        for j in range(2,sr+1):
            if number%j==0:
                prime = False
                break
    if prime == True:
        print("Prime")
    else:
        print("Not prime")
            
